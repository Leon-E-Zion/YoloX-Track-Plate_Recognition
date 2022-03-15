import cv2


# ==========================================================
# 绘图函数  根据 神经网络的处理结果  对原图进行标注 返回标注好的图片
def draw_new(image, obj_list,line, line_thickness=None):
    # print(obj_list) {'bbox': [1002, 219, 1202, 297], 'cls': 'car', 'car_num': '-->Null', 'center': [1102, 258], 'redline': 'nothing', 'object_v': 'v=22.25--> Too-Fast'}
    # Plots one bounding box on image img
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    obj_base_mes = obj_list['base_mes']
    for mes_obj_id in obj_base_mes:
        mes_obj = obj_base_mes[mes_obj_id]
        # print(mes_obj)
        color = (0, 0, 255)
        x1,y1,x2,y2 = mes_obj['bbox']
        c1, c2 = (x1, y2), (x2, y1)
        cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)  # font thickness
        cls = mes_obj['cls']
        t_size = cv2.getTextSize(cls, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
        # 绘制的数据标注
        mes_plot = ''
        if 'car_num' in mes_obj:
            mes_plot += mes_obj['car_num']
        else:
            mes_plot += ' '
        mes_plot += '-'
        if 'object_v' in mes_obj:
            mes_plot += mes_obj['object_v']
        else:
            mes_plot += ' '
        mes_plot += '-'
        if 'reflect' in mes_obj:
            mes_plot += mes_obj['reflect']
        else:
            mes_plot += ' '

        if 'over_line' in mes_obj:
            mes_plot += mes_obj['over_line']
        else:
            mes_plot += ' '



        cv2.putText(image, '{}'.format((mes_plot)), (c1[0]-2, c1[1] - 2), 0, tl / 3,
                        [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
    # 线条绘制
    # print(line)#[904, 987, 1059, 742]
    add_0 = (line[0],line[1])
    add_1 = (line[2], line[3])
    add_2 = (line[4],line[5])
    add_3 = (line[6], line[7])
    cv2.line(image,add_0,add_1,color=(255,0,0),thickness=3)
    cv2.line(image,add_2,add_3,color=(255,0,0),thickness=3)
    return image
# ==========================================================