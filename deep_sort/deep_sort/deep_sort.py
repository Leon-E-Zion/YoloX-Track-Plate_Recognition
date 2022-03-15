# =====================================================
# 引用一些必要的包
import numpy as np
import torch

from .deep.feature_extractor import Extractor
from .sort.nn_matching import NearestNeighborDistanceMetric
from .sort.preprocessing import non_max_suppression
from .sort.detection import Detection
from .sort.tracker import Tracker

from hyperlpr import *
__all__ = ['DeepSort']
# =====================================================

# =====================================================================================================================================================================================
# 定义 DeepSort的类
class DeepSort(object):
    # =============================================================================================================================================================
    # 初始化 一些 DeepSort 所必须的参数
    def __init__(self, model_path, max_dist=0.2, min_confidence=0.3, nms_max_overlap=1.0, max_iou_distance=0.7, max_age=70, n_init=3,nn_budget=100, use_cuda=True):
        # 置信度阈值
        self.min_confidence = min_confidence
        # IoU 抑制 --> 重复框 删除作用
        self.nms_max_overlap = nms_max_overlap
        # 基于框格对图片进行扣取目标的函数的初始化
        self.extractor = Extractor(model_path, use_cuda=use_cuda)
        # 定义 车牌 收集器
        self.plate_nums ={}
        # 定义 余弦函数的 阈值
        max_cosine_distance = max_dist
        nn_budget = nn_budget
        # 定义 计算特征图的距离函数的选择
        metric = NearestNeighborDistanceMetric(
            "cosine", max_cosine_distance, nn_budget)
        # 定义 追踪器
        self.tracker = Tracker(metric, max_iou_distance=max_iou_distance, max_age=max_age, n_init=n_init)
    # =============================================================================================================================================================



    # =============================================================================================================================================================
    # 定义 更新函数 追踪数据更新
    def update(self, bbox_xywh, confidences, clss, ori_img):
        # 获取原图的尺度 信息
        self.height, self.width = ori_img.shape[:2]

        # ================================================================================================================================================
        # 输入 数据 获取追踪的信息
        features = self._get_features(bbox_xywh, ori_img)
        bbox_tlwh = self._xywh_to_tlwh(bbox_xywh)
        detections = [Detection(bbox_tlwh[i], clss[i], conf, features[i]) for i, conf in enumerate(confidences) if conf > self.min_confidence]
        # ================================================================================================================================================

        # ========================================
        # 跟踪数据的刷新
        self.tracker.predict()
        self.tracker.update(detections)
        # ========================================

        # ===========================================================================================
        # 获取追踪器的最终输出 --> 这里对于 deepsort和车牌的改动太多了 之后好好解释一下
        outputs = []

        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            box = track.to_tlwh()
            x1, y1, x2, y2 = self._tlwh_to_xyxy(box)
            cls_ = track.cls_
            track_id = "{}".format(track.track_id)
            # 对车牌 的追踪进行 锁定 ---> 这里之后好好给解释一下
            if track.cls_ == 'car' or 'track':
                face = ori_img[y1:y2, x1:x2]
                a = HyperLPR_plate_recognition(np.array(face))
                if a:
                    confidence = a[0][1]
                    if confidence >= 0.8:
                        track_id = "{}".format(track.track_id) + '-->' + a[0][0][1:]
                        self.plate_nums["{}".format(track.track_id)] = "{}".format(track_id)
                    if "{}".format(track.track_id) in self.plate_nums:
                        track_id = self.plate_nums["{}".format(track.track_id)]

            outputs.append((x1, y1, x2, y2, cls_, track_id))

        return outputs
    # =============================================================================================================================================================


    # ==================================================================================
    # 定义的 各种 框格的格式转化函数
    @staticmethod
    def _xywh_to_tlwh(bbox_xywh):
        if isinstance(bbox_xywh, np.ndarray):
            bbox_tlwh = bbox_xywh.copy()
        elif isinstance(bbox_xywh, torch.Tensor):
            bbox_tlwh = bbox_xywh.clone()
        bbox_tlwh[:, 0] = bbox_xywh[:, 0] - bbox_xywh[:, 2]/2.
        bbox_tlwh[:, 1] = bbox_xywh[:, 1] - bbox_xywh[:, 3]/2.
        return bbox_tlwh

    def _xywh_to_xyxy(self, bbox_xywh):
        x, y, w, h = bbox_xywh
        x1 = max(int(x-w/2), 0)
        x2 = min(int(x+w/2), self.width-1)
        y1 = max(int(y-h/2), 0)
        y2 = min(int(y+h/2), self.height-1)
        return x1, y1, x2, y2

    def _tlwh_to_xyxy(self, bbox_tlwh):
        """
        TODO:
            Convert bbox from xtl_ytl_w_h to xc_yc_w_h
        Thanks JieChen91@github.com for reporting this bug!
        """
        x, y, w, h = bbox_tlwh
        x1 = max(int(x), 0)
        x2 = min(int(x+w), self.width-1)
        y1 = max(int(y), 0)
        y2 = min(int(y+h), self.height-1)
        return x1, y1, x2, y2

    def _xyxy_to_tlwh(self, bbox_xyxy):
        x1, y1, x2, y2 = bbox_xyxy

        t = x1
        l = y1
        w = int(x2-x1)
        h = int(y2-y1)
        return t, l, w, h
    # ==================================================================================


    # ====================================================
    # 根据框格与 原图 进行抠图
    def _get_features(self, bbox_xywh, ori_img):
        im_crops = []
        for box in bbox_xywh:
            x1, y1, x2, y2 = self._xywh_to_xyxy(box)
            im = ori_img[y1:y2, x1:x2]
            im_crops.append(im)
        if im_crops:
            features = self.extractor(im_crops)
        else:
            features = np.array([])
        return features
    # ====================================================
