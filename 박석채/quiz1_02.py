""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""

num1 = int(input('첫번째 수를 입력 :'))
num2 = int(input('첫번째 수를 입력 :'))
operator = input('연산기호를 입력 :')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else: print('연산기호를 잘못 입력하셨습니다.')