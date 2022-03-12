# ========================================================================|
# 导入一些必要的包 ==> 初始化环境
import numpy as np

from AIDetector_pytorch import Detector
import imutils
import time
from utils_leon import *
import os
# ========================================================================|
class Leon_detect():
<<<<<<< HEAD
=======

>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
    def __init__(self):
        # ===========================================|
        # ===========================================|
        # |关于 视频 处理 的一些超参数|
        # ========================
        # ---处理的视频的路径 为0 为调用本地摄像头 √-------
        self.video = 'a.flv'
        # -----------初始 行人数量 √-------------------
        self.passer_num = 0
        # ------------根路径 运行环境 √----------------
        self.root = os.getcwd()
        # --------------跳帧参数 √--------------------
<<<<<<< HEAD
        self.fps_skip = 1
=======
        self.fps_skip = 4
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
        # ===========================================|
        # ===========================================|
        # |--|
        # |--|
        # |--|
        # |--|
        # =========================================================================|
        # =========================================================================|
        # |图像分析的函数的一些参数|
        # =====================
        # -----------------过往流量记录 时间间隔  单位 s----------------
<<<<<<< HEAD
        self.passer_note_time = 100000
=======
        self.passer_note_time = 10
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
        # ----------------保存的图像的大小尺寸----------------
        self.height = 500
        # ----------------测速函数----------------
        self.get_v = True
        self.v_max = 3
        self.v_norm = 200
        self.v_bias = 3
        # ----------------天气函数----------------
        self.area = ['shenzhen']
        # ----------------嫌疑车辆追踪----------------
        self.get_clime = True
        # 是否已经发现嫌疑车辆
        self.tar_get = False
        self.tar_car_nums = ['1111','2222']
        # ----------------光照增强----------------
        self.light_improve = False
        # ----------------人流量与车流量----------------
        self.person_num = 0
        self.traffic_tools_num = 0
        # ----------------数据库 存储 一些 用于可视化的 信息----------------
        self.obj_list = {}
        # ----------------用于 机器学习方法预测人/车 流量----------------
        self.mes_machine = None
        self.machine_predict = True
        self.csv_root_train = os.path.join(self.root, 'train.csv')
        self.csv_root_pre = os.path.join(self.root, 'pre.csv')
        self.pre_mes = []
<<<<<<< HEAD
        # 画线
        self.line = []
        # 逆行检测
        self.old_boxes = None
        self.tar_area_boxes = []
=======
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
    # =========================================================================|
    # =========================================================================|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # =========================================================================|
    # =========================================================================|
<<<<<<< HEAD
    def line_get_(self,im):
        self.line_img = im
        line = line2get2plot(self.line_img)
        for num in line[1]:
            self.line.append(int(num))
    def area_get(self,im):
        self.line_img = im
        line = line2get2plot(self.line_img)
        for num in line[1]:
            self.tar_area_boxes.append(int(num))
    # =========================================================================|
    # =========================================================================|
=======
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
    # |天气模块|
    # ========
    # ---------------------------获取天气--------------------------
    def wh_get(self):
        whe ,temp_high ,temp_low ,change ,wind_idr ,wind_power = get_wh_mes(self.area)
        return [whe ,temp_high ,temp_low ,change ,wind_idr ,wind_power]
    # =========================================================================|
    # =========================================================================|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # |--|
    # =======================================================================================================|
    # =======================================================================================================|
    # |定义主函数|
    # =========
    # -------------------------------- 主要运行部分--------------------------
    def main(self):
        # ===============================================================|
        # |其他|
        # =====
        # ---获取 开始运行的时间---
        time_start = time.time()
        # --定义展示窗口的名字--
        name = 'demo'
        # ----定义检测器----
        det = Detector()
        # ===============================================================|
        # |--|
        # |--|
        # |--|
        # |--|
        # ===============================================================|
        # |关于 视频流数据的获取|
        # ===================
        # 图片获取 <-- 拆解为图片 <-- 从OpenCV读入视频
        cap = cv2.VideoCapture(self.video)
        # 获取 视频帧率==>感觉 这些东西可以使用NoteBook进行一个详细的解释
        fps = int(cap.get(5))
        print('fps:', fps)
        t = int(1000 / fps)
        videoWriter = None
        # ===============================================================|
        # |--|
        # |--|
        # |--|
        # |--|
        # ==============================|
        # 关于帧率的控制 参数
<<<<<<< HEAD
        pic_i = 0
=======
        i = 0
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
        # 控制 机器学习 预测部分的参数
        i_= 0
        # ==============================|
        # |--|
        # |--|
        # |--|
        # |--|
        # ===============================================================
        # 开始对图片的迭代 处理
        while True:
            # =====================
            # 逐张地获取图片
            _, im = cap.read()
            # =====================
<<<<<<< HEAD
            if pic_i == 0:
                #
                self.line_get_(im)
                self.line_get_(im)
                #
                self.area_get(im)
                self.area_get(im)

            # 获取线条 --> [908, 283, 1497, 312]
            # =====================
=======
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
            # |--|
            # |--|
            # 光照提升
            if self.light_improve:
                im = light_improve(im)
            # =====================
            # |--|
            # |--|
            # =================================================
            # 跳帧处理
<<<<<<< HEAD
            pic_i += 1
            if pic_i % self.fps_skip != 0:
=======
            i += 1
            if i % self.fps_skip != 0:
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
                continue
            if im is None:
                break
            # =================================================
            # |--|
            # |--|
            # ===============================================================================
            # |机器学习预测|
            # ===========
            # 时间函数 --> 数据写入csv
<<<<<<< HEAD
            if pic_i >= 1:
                if self.machine_predict:
                    time_now = time.time()
                    time_distance = time_now - time_start
                    if time_distance >= self.passer_note_time:
                        i_+=1
                        # 计算 单位时间内的总 流量
                        self.passer_num += result_['passer_num']
                        # 获取各类数据
                        mes = self.wh_get()
                        time_distance = time_distance
                        mes.append(time_distance)
                        mes.append(self.person_num)
                        mes.append(self.traffic_tools_num)
                        mes.append(self.passer_num)
                        # print(mes)# ['多云', '17', '25', '微风', '东风', '1级', 10.094501733779907, 0, 1, 0]
                        pre_mes = [mes,mes,mes,mes]
                        self.pre_mes.append(mes)
                        data_noting(self.pre_mes, self.csv_root_train)
                        data_noting(pre_mes, self.csv_root_pre)
                        if i_ % 10 == 0:
                            a = get_train_pre(self.csv_root_train, self.csv_root_pre)
                            print('Now Passer_Num is {}'.format(a))
=======
            if self.machine_predict:
                time_now = time.time()
                time_distance = time_now - time_start
                if time_distance >= self.passer_note_time:
                    i_+=1
                    # 计算 单位时间内的总 流量
                    self.passer_num += result_['passer_num']
                    # 获取各类数据
                    mes = self.wh_get()
                    time_distance = time_distance
                    mes.append(time_distance)
                    mes.append(self.person_num)
                    mes.append(self.traffic_tools_num)
                    mes.append(self.passer_num)
                    # print(mes)# ['多云', '17', '25', '微风', '东风', '1级', 10.094501733779907, 0, 1, 0]
                    pre_mes = [mes,mes,mes,mes]
                    self.pre_mes.append(mes)
                    data_noting(self.pre_mes, self.csv_root_train)
                    data_noting(pre_mes, self.csv_root_pre)
                    if i_ % 10 == 0:
                        a = get_train_pre(self.csv_root_train, self.csv_root_pre)
                        print('Now Passer_Num is {}'.format(a))
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
            # ===============================================================================
            # |--|
            # |--|
            # =============================================================================================================================================================
            # |获取 分析器 根据原图进行神经网络分析 得到的数据 进而 标注好的图片|
            # =======================================================
<<<<<<< HEAD
            if 1: # 关于调试的时候 此处一定要修改
=======
            try : # 关于调试的时候 此处一定要修改
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
                # ==========================
                result_ = det.feedCap(im)
                # print(result_)
                # ==========================
                # 处理好的图片
                result = result_['frame']
                # 所有目标的框格
<<<<<<< HEAD
                tar_bboxes_mes = result_['bboxes_mes'] # 【[x1, y1, x2, y2,int(track_id),cls_,car_num]】
                for i,tar_bbox_mes in enumerate(tar_bboxes_mes):
                    box = tar_bbox_mes[0:4]
                    # print(box) # [1100, 135, 1151, 172]
                    tar_bboxes_mes[i].append(get_center(box))
                    # =====================判定是否过红线===================================================
                    # print(self.line) # [149, 534, 1322, 536, 1326, 591, 151, 587] x,y,x,y,x,y,x,y
                    y_center_0 = (self.line[1]+self.line[3])*0.5
                    y_center_1 = (self.line[5]+self.line[7])*0.5
                    y_centers = np.array([y_center_0,y_center_1])
                    y_min = np.min(y_centers)
                    y_max = np.max(y_centers)
                    if tar_bboxes_mes[i][5] == 'person':
                        tar_bboxes_mes[i].append('nothing')
                    elif tar_bboxes_mes[i][-1][1] < y_max and tar_bboxes_mes[i][-1][1] > y_min:
                        tar_bboxes_mes[i].append('error')
                    else:
                        tar_bboxes_mes[i].append('nothing')
                    tar_bboxes_mes[i].append(0)
                    # tar_bboxes_mes[i]-->[[423, 397, 480, 505, 6, 'person', '-->Null', center = [451, 451],condition,k]]
                # =================================================================================
                # # =====================================逆行检测==========================
                self.area = self.tar_area_boxes
                x1 = np.min(np.array([self.area[0],self.area[2],self.area[4],self.area[6]]))
                x2 = np.max(np.array([self.area[0],self.area[2],self.area[4],self.area[6]]))
                y1 = np.min(np.array([self.area[1],self.area[3],self.area[5],self.area[7]]))
                y2 = np.max(np.array([self.area[1],self.area[3],self.area[5],self.area[7]]))
                if pic_i >= 1 :
                    if self.old_boxes != None:
                        for i, tar_bbox_mes_new in enumerate(tar_bboxes_mes):
                            center_new = tar_bbox_mes_new[7]
                            # 判断车辆是否在管区内
                            if center_new[0] > x1 and center_new[0] < x2 and center_new[1] > y1 and center_new[1] < y2:
                                for i, tar_bbox_mes_old in enumerate(self.old_boxes):
                                    id_new = tar_bbox_mes_new[4]
                                    id_old = tar_bbox_mes_old[4]
                                    if id_old==id_new:
                                        # 可以得到id号
                                        center_old = tar_bbox_mes_old[7]
                                        center_new = tar_bbox_mes_new[7]
                                        k = get_direction(center_old,center_new)
                                        # 获取每辆车的斜率
                                        normal_k = -9
                                        # 获取偏移角
                                        degree = direction_ajust(normal_k, k)
                                        if degree < 0 :
                                            tar_bboxes_mes[i][9] = 'reflect'
                                        # tar_bboxes_mes[i]-->[[423, 397, 480, 505, 6, 'person', '-->Null', center = [451, 451],condition,k]]
                # 对比斜率



                # 所有目标的 图片
                tar_figures = result_['tar_figures'] # ([face, track_id],[face, track_id])
                # 刷新老框数
                self.old_boxes = tar_bboxes_mes
=======
                tar_bboxes_mes = result_['bboxes_mes'] # [[x1, y1, x2, y2,int(track_id),cls_,car_num]]
                # 所有目标的 图片
                tar_figures = result_['tar_figures'] # ([face, track_id],[face, track_id])
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
                # ================================================各种函数功能==============================
                # |--|
                # |--|
                # =================================================================================
                if self.get_v:
                # 测速功能
                    for bbox_mes in tar_bboxes_mes:
                        id = bbox_mes[4]
                        for bbox_mes_old in tar_bboxes_mes_old:
                            id_ = bbox_mes_old[4]
                            if id_ == id:
                                # 标注信息之一 逐个获取 速度
                                v = get_v(bbox_mes, bbox_mes_old, self.v_max,self.v_norm,self.v_bias)
                                v_data = {'{}'.format(id_):v}
                                self.obj_list.update(v_data)
                # 数据刷新
                tar_bboxes_mes_old = tar_bboxes_mes
                # =================================================================================
                # |--|
                # |--|
                # ===============================================================================
                # |检查嫌疑车辆 识别到便拍照记录 与 标注|
                # ================================
                if self.get_clime:
                    # 标注信息之一
                    aa = get_clime(self.tar_car_nums, tar_bboxes_mes, tar_figures, self.root)
                    if aa != []:
                            self.tar_get = True
                    if self.tar_get :
                        print('出现嫌疑车辆')
                # ===============================================================================
                # |--|
                # |--|
                # ===============================================================================
                # 视角中经过的对象数
                self.passer_num  += result_['passer_num']
                # ===============================================================================
                # |--|
                # |--|
                # ===============================================================================
                # 当前场景 密度估计模块
                self.person_num = get_dense(['person'], tar_bboxes_mes)
                self.traffic_tools_num = get_dense(['truck','car','bus'], tar_bboxes_mes)
                # ===============================================================================
                # |--|
                # |--|
                # ====================================================================================================================================================
                # 相关数据的绘制
                if self.get_v:
                    for mes in self.obj_list:
                        # print(mes){'1': '16--> Too-Fast', '2': '28--> Too-Fast', '4': '40--> Too-Fast', '6': '10--> Too-Fast'}
                        for i,mes_ in enumerate(tar_bboxes_mes):
                            if str(mes_[4]) == str(mes):
                                tar_bboxes_mes[i][5]= (self.obj_list[mes])
                    # print(tar_bboxes_mes) # [[470, 2, 681, 189, 1, 'car', '-->W120', '16--> Too-Fast'], [909, 183, 1191, 474, 2, 'car', '-->2N96', '26--> Too-Fast']]
<<<<<<< HEAD
                    result = draw_new(result, tar_bboxes_mes,self.line)
=======
                    result = draw_new(result,tar_bboxes_mes)
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
                # ====================================================================================================================================================
                # |--|
                # |--|
            # ======================
<<<<<<< HEAD
            # except:
            #     result = im
=======
            except:
                result = im
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
            # ======================
            # |--|
            # |--|
            # =======================================================================
            # 将图片 处理成指定的大小 ==> 展示的美观问题
            result = imutils.resize(result, height=self.height)
            # 关于图片 收集成 视频文件 进行存储
            if videoWriter is None:
                fourcc = cv2.VideoWriter_fourcc(
                    'm', 'p', '4', 'v')  # opencv3.0
                videoWriter = cv2.VideoWriter(
                    'result.mp4', fourcc, fps, (result.shape[1], result.shape[0]))
            videoWriter.write(result)
            # 关于处理好的图片的可视化
            cv2.imshow(name, result)
            cv2.waitKey(t)
            # 设置退出 展示 退出 处理的按钮  ==> 点 "x"  退出
            if cv2.getWindowProperty(name, cv2.WND_PROP_AUTOSIZE) < 1:
                # 点x退出
                break
            # =======================================================================
            # |--|
            # |--|
<<<<<<< HEAD
        # =======================================================================
        # 关于 视频流的 一些基础设置
        cap.release()
        videoWriter.release()
        cv2.destroyAllWindows()
        # =======================================================================
=======
        # =======================================================================
        # 关于 视频流的 一些基础设置
        cap.release()
        videoWriter.release()
        cv2.destroyAllWindows()
        # =======================================================================
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f


if __name__ == '__main__':
    a = Leon_detect()
    a.main()