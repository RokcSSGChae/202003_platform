"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""

score = int(input('점수를 입력하세요 : '))

if score in range(81,101):
    print('당신의 학점은 A입니다.')
elif score in range(61,81):
    print('당신의 학점은 B입니다.')
elif score in range(41,61):
    print('당신의 학점은 C입니다.')
elif score in range(21,41):
    print('당신의 학점은 D입니다.')
elif score in range(0,21):
    print('당신의 학점은 F입니다.')
else:
    print('학점을 잘못 입력하셨습니다.')