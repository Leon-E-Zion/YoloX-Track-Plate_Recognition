import math

def get_direction(center_old,center_new):
    # 获取坐标
    x_old = center_old[0]
    y_old = center_old[1]
    x_new = center_new[0]
    y_new = center_new[1]
    k = round(((y_new - y_old)/((abs((x_new - x_old)))+0.0001)),2)
    return k

def direction_ajust(normal_k,k):
    k_dis = (k-normal_k)/(1+k*normal_k)
    degree = math.degrees(math.atan(k_dis))
    return degree

# normal_k = 1
# center_old = [451, 451]
# center_new = [900,900]
# k  = get_direction(center_old,center_new)
#
# print(direction_ajust(normal_k,k)) --> 0