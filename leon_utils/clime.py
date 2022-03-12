import cv2
import uuid
import os


def pic_save(tar_num,pic,root):
    root = os.path.join(root,'clime_pics')
    file_name = os.path.join(root,tar_num)
    if not os.path.exists(file_name ):
        os.mkdir(file_name)
    ran = uuid.uuid4().hex
    pic_name = os.path.join(file_name , '{}.jpg'.format(ran))
    cv2.imwrite(pic_name,pic)


# tar为目标车牌号的后4位
def get_clime(tars,figures_mes,figures,root):
    id_list = []
    for figure_mes in figures_mes:
        # 发现目标车牌
        if figure_mes[6][-4:] in tars:
            tar_id = figure_mes[4]
            # 获得车辆照片
            i = 0
            for figure in figures:
                i += 1
                id = figure[1]
                if id == tar_id:
                    id_list.append(id)
                    pic = figure[0]
                    pic_save(figure_mes[6][-4:],pic,root)
    return  id_list

