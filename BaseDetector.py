# ===================================
# 引入一些必要的 包
from tracker import update_tracker
import cv2


# ===================================

# =================================================================================
# 定义一个基础的检测类  这个 类 对应的对象 输出的结果中 直接包含了 用于展示的图片
class baseDet(object):

    # ========================================
    # 定义 一些需要用到的相关的参数 ==> Python语法
    def __init__(self):
        # 定义 Stride 输入图片的下采样系数
        self.stride = 1

    # ========================================

    # ================================================
    # 变量容器的 初始化函数  创建各类变量容器
    def build_config(self):
        # 定义一些变量 作为中间变量  容器作用  数据的存储
        self.faceTracker = {}
        self.faceClasses = {}
        self.faceLocation1 = {}
        self.faceLocation2 = {}
        self.frameCounter = 0
        self.currentCarID = 0
        self.recorded = []
        # 定义 绘图时使用的字体
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    # ================================================

    # ==================================================================================
    def feedCap(self, im):
        # ==============================
        # 定义一个 变量容器 字典
        retDict = {'frame': None,
                   'faces': None,
                   'list_of_ids': None,
                   'face_bboxes': [],
                   'bboxes_mes':[],
                   'passer_num':None}
        # ==============================

        # ========================
        # 图片帧数的 定义
        self.frameCounter += 1
        # ========================

        # ==============================================================
        # 获取 图片分析器的 输出 ==> 这里的输出 是 包含之后可以直接 展示的图片
        im, tar_figures, tar_bboxes,bboxes_mes,passer_num = update_tracker(self, im)
        # ==============================================================

        # =============================================================================
        # 将 数据分析器 获取的数据 进行包装 包装成一个列表 返回到 demo.py 的 main 函数中
        # 这是处理好后 可以直接展示的原图
        retDict['frame'] = im
        # 将 检测器得到的 各个框 进行收集
        retDict['tar_bboxes_mes'] = tar_bboxes
        # 将 检测器得到的 各个框 进行收集  依据他们在原图上将 框中的内容抠出来 合并到一起 ==> faces
        retDict['tar_figures'] =  tar_figures
        retDict['bboxes_mes'] = bboxes_mes
        retDict['passer_num'] = passer_num
        # =============================================================================

        # 数据返回
        return retDict

    # ==================================================================================
    # 定义一些函数  捕捉 会导致报错的 情况
    def init_model(self):
        raise EOFError("Undefined model type.")

    def preprocess(self):
        raise EOFError("Undefined model type.")

    def detect(self):
        raise EOFError("Undefined model type.")
    # ==================================================================================
