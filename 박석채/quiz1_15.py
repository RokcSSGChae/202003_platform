"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오.
(리스트 split 과 슬라이싱 활용) """

resident_num = input("주민등록번호를 입력하세요 : ")

sex = resident_num[-7]

if sex in ('1','3'):
    print('남자입니다.')
elif sex in ('2','4'):
    print('여자입니다.')
else: print('잘못 입력하셨습니다.')