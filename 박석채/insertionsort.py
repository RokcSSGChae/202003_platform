def insertion_sort(list):
    for j in range(1, len(list)):
        key = list[j] ## j는 비교하려는 값의 위치 key는 그 값
        i = j-1 ## i는 바로 이전 값을 가리키는 위치
        while i>=0 and list[i] > key: ## 값을 넣기 위해 찾는 과정
            list[i+1] = list[i] ## 조건 맞으면 swap
            i = i-1
        list[i+1] = key
    return list

list = [9,4,3,1,12]
print(insertion_sort(list))
