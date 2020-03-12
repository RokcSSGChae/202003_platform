"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""

n_dan = int(input("구구단 단수를 입력 : "))

for i in range(1,10) :
    print('{}X{}={}'.format(n_dan, i, n_dan*i))