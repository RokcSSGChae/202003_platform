def selection_sort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

list = [9,4,3,1,12]
print(selection_sort(list))


