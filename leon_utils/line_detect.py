# coding: utf-8
import cv2
import numpy as np
import os
def line_get(img):
    xy_box = []
    # print img.shape

    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        coord = None
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
            coord = [x,y]
            if coord != None:
                xy_box.append(coord)
            if len(xy_box) == 2 :
                for coord_ in xy_box:
                    for coord_num in coord_:
                        with open('line_get.txt', 'a') as wf:
                            wf.write('{}\n'.format(coord_num))

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    while (True):
        try:
            cv2.waitKey(100)
        except Exception:
            cv2.destroyWindow("image")
            break
        if len(xy_box) == 2:
            break
    # cv2.waitKey(0)
    # cv2.destroyAllWindow()


    return (xy_box)

# line_get()

def line_plot(xy_boxes,img):

    xy_0 = (int(xy_boxes[0]),int(xy_boxes[1]))
    xy_1 = (int(xy_boxes[2]),int(xy_boxes[3]))

    cv2.line(img,xy_0,xy_1,color=(255,0,0))
    cv2.imwrite('test.jpg',img)
    return img,[int(xy_boxes[0]),int(xy_boxes[1]),int(xy_boxes[2]),int(xy_boxes[3])]

def line2get2plot(pic):
    # box记录中转 --> line_get.txt
    if os.path.exists('line_get.txt') :
        os.remove('line_get.txt')
    # 获取图片
    image = pic
    # 获取 点击 坐标
    line_get(image)
    # 获取框
    f = open("line_get.txt", encoding="utf-8")
    # f.read() --》 [[24, 464], [1245, 455]]
    xy_boxes = f.read()
    f.close()
    # print(xy_boxes)
    box = []
    box = xy_boxes.split('\n')
    box = box[:-1]
    box_ = []
    for num in box:
           box_.append(int(num))
    # 画图函数
    an = line_plot(box,image)

    return an

# line2get2plot()

