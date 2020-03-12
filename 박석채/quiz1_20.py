"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고,
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""

def game_369(a):
    num = str(a)
    data = list(num)
    for data in num:
        if '3' in data or '6' in data or '9' in data:
            return True
    return False

for i in range(1,101):
    if game_369(i) == True:
        print('짝', end= ' ')
    elif i%5 == 0:
        print('아자', end= ' ')
    else:
        print(str(i), end = ' ')
    if i%20 ==0:
        print()
