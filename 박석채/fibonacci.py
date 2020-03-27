def is_natural(num):
    if int(num) == num and num > 0:
        return True
    else: return False

def fibonacci(num):
    if not is_natural(num):
        print("잘못 입력하셨습니다")
    else:
        ret = 1
        if num > 2:
            ret = fibonacci(num - 1) + fibonacci(num - 2)
        return ret

print(fibonacci(10)) ## 55
