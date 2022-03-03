import numpy as np
import argparse
import cv2

def light_improve(img):
    image = img
    (B, G, R) = cv2.split(image)
    imageBlueChannelAvg = np.mean(B)
    imageGreenChannelAvg = np.mean(G)
    imageRedChannelAvg = np.mean(R)
    K = (imageRedChannelAvg+imageGreenChannelAvg+imageRedChannelAvg)/3;
    Kb = K/imageBlueChannelAvg;
    Kg = K/imageGreenChannelAvg;
    Kr = K/imageRedChannelAvg
    B = cv2.addWeighted(B, Kb, 0, 0, 0)
    G = cv2.addWeighted(G, Kg, 0, 0, 0)
    R = cv2.addWeighted(R, Kr, 0, 0, 0)
    image_new = cv2.merge([B, G, R])

    return image_new



