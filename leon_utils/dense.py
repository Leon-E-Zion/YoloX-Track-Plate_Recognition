def get_dense(cls,mes):
    i = 0
    for mes_ in mes:
        if mes_[5] in cls:
            i+=1
    return i