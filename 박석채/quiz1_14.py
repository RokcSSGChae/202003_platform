"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""

letter = input('문자를 입력하세요 : ')

U = letter.upper()
L = letter.lower()

if U == L:
    print("입력 형식이 잘못되었습니다")
elif letter == U:
    print(L)
elif letter == L:
    print(U)



