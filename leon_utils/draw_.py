import cv2


# ==========================================================
# 绘图函数  根据 神经网络的处理结果  对原图进行标注 返回标注好的图片
<<<<<<< HEAD
def draw_new(image, bboxes,line, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    for (x1, y1, x2, y2, cls_id, v,car_num,center,condition,k) in bboxes:
=======
def draw_new(image, bboxes, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    for (x1, y1, x2, y2, cls_id, v,car_num) in bboxes:
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
        if cls_id in ['person']:
            color = (0, 0, 255)
        # 'car' or'truck' or 'bus'
        else:
            cls_id = 'Traffic Tools'
            color = (0, 255, 0)

        c1, c2 = (x1, y2), (x2, y1)
        cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
<<<<<<< HEAD

        if condition == 'error':
            mes = '{}-{}'.format(v,'error')
        else:
            mes = '{}-{}'.format(v,'normal')

        if k == 'reflect':
            mes += '--reflect'
        else:
            pass
        cv2.putText(image, '{}'.format((mes)), (c1[0]-2, c1[1] - 2), 0, tl / 3,
                        [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
    # print(line)#[904, 987, 1059, 742]
    add_0 = (line[0],line[1])
    add_1 = (line[2], line[3])
    add_2 = (line[4],line[5])
    add_3 = (line[6], line[7])
    cv2.line(image,add_0,add_1,color=(255,0,0),thickness=3)
    cv2.line(image,add_2,add_3,color=(255,0,0),thickness=3)
=======
        cv2.putText(image, '{}'.format(v), (c1[0]-2, c1[1] - 2), 0, tl / 3,
                    [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
>>>>>>> a87c9243c9c1e03932e93b77be9ea3c13ae2ce3f
    return image
# ==========================================================