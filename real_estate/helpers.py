import numpy as np

def log_with_zeros(lst):
    log_lst = []
    for i in lst:
        if i <= 0:
            log_lst.append(-5.5)
        else:
            log_lst.append(np.log(i))
    return log_lst

def log_without_zeros(lst):
    lst = [i for i in lst if i > 0]
    log_lst = []
    for i in lst:
        log_lst.append(np.log(i))
    return log_lst

def standard_scale_without_zeros(lst, return_zeros):
    positive_list = [i for i in lst if i > 0]
    mean = np.mean(positive_list)
    sd = np.std(positive_list)
    if return_zeros:
        scaled_list = (lst-mean)/sd
    else:
        scaled_list = (positive_list-mean)/sd
    return {"values":scaled_list,
            "mean":mean,
            "sd":sd}

def standard_scale(lst):
    mean = np.mean(lst)
    sd = np.std(lst)
    scaled_lst = (lst-mean)/sd
    return {"values":scaled_lst,
            "mean":mean,
            "sd":sd}

def keep_positive(lst):
    return [i for i in lst if i > 0]
