"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""

num = int(input('숫자를 입력하세요 :'))

for i in range(1, num+1):
    print(' '*(num-i), '★'*i)
for i in range(1, num):
    print(' '*i, '★'*(num-i))
