def hanoi(n, start, end):
    if n == 1:
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(start, n, end))
    else:
        mid = 6 - start - end
        hanoi((n-1), start, mid)
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮긴다.".format(start, n, end))
        hanoi((n-1), mid, end)

hanoi(3,1,3)

