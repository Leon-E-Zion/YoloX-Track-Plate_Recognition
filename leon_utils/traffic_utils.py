import numpy as np
import cv2
import math

def get_center(bbox):
    center = [int((bbox[0]+bbox[2])*0.5),int((bbox[1]+bbox[3])*0.5)] # x,y
    return center

def get_center_distance(center_0,center_1):
    distance = int((abs(center_0[0]-center_1[0])**2 + abs(center_0[1]-center_1[1])**2) ** 0.5)
    return distance

def get_v(bbox_mes_0,bbox_mes_1,v_max,v_norm,v_bias):
    if bbox_mes_0[5] != 'person':
        center_0 = get_center(bbox_mes_0)
        # print(bbox_mes_0[0][0])
        center_1 = get_center(bbox_mes_1)
        v = get_center_distance(center_0 ,center_1)
        v = round(math.exp(v/v_norm)**2*2 +  math.exp(v_bias),2)
        if v >= v_max:
            v = 'v='+str(v)+'--> Too-Fast'
    else:
        v = ' '
    return str(v)
# # example
# a = [[746, 453, 998, 637, 1]]
# b = [[752, 443, 998, 622, 1]]
# num = get_v(a,b,2)
# print(num)

def xyxy2xywh(location):
    x = (location[0]+location[2])*0.5
    y = (location[1] + location[3]) * 0.5
    w = location[2] - location[0]
    h = location[3] - location[1]
    return [x,y,w,h]

def estimateSpeed(location2, location1,v_max,v_norm,v_bias):
    location1 = xyxy2xywh(location1)
    location2 = xyxy2xywh(location2)
    d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
    # carWidht = 2
    # ppm = location2[2] / carWidht
    ppm = 10
    d_meters = d_pixels / ppm
    speed = d_meters * 10 * 3.6
    speed = (speed/v_norm)+  math.exp( v_bias )
    return speed
