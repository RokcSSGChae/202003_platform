def quick_sort(list):
    if len(list) <= 1:
        return list
    g1, piv, g2 = [], [], []
    piv_num = list[-1]
    for num in list:
        if num < piv_num:
            g1.append(num)
        elif num > piv_num:
            g2.append(num)
        else:
            piv.append(num)
    ret = quick_sort(g1) + piv + quick_sort(g2)
    return ret

list = [6,8,3,9,10,1,2,4,7,5]
print(quick_sort(list))


