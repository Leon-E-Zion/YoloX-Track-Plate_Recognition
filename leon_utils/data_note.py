#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 导入CSV安装包
import csv
import random
import numpy as np

def data2num(str_):
    ascll = np.fromstring(str(str_), dtype=np.uint8)
    num_ = 0
    for num in ascll:
        num_ += num ** 0.7
    return round(num_, 2)

def datas2nums(str_s):
    str_s_new = []
    for str_ in str_s:
        str_ = data2num(str_)
        str_s_new.append((str_))
    return str_s_new
def data_get(a,b,c,d,e,f,g,h,i,j,k):
    mes = [a,b,c,d,e,f,g,h,i,j,k]
    return mes

def data_get_random():
    mes = []
    for da in range(10):
        mes.append(random.randint(10,100))
    return mes


def data_noting(mes,root):
    # 1. 创建文件对象
    f = open(root,'w',encoding='utf-8',newline="")
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头

    # 4. 写入csv文件内容
    for mes_ in mes:

        mes_=datas2nums(mes_)
        csv_writer.writerow(mes_)

    # 5. 关闭文件
    f.close()
    return 0

# root = 'a.csv'
# mes = [['多云', '17', '25', '微风', '东风', '1级', 10.094501733779907, 0, 1, 0]]
# data_noting(mes,root)