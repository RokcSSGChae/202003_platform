def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1): ## 가장 큰 값을 하나씩 제외하므로
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] ## 앞에 값이 크면 swap
    return list

list = [7,4,5,1,3]
print(bubble_sort(list))


