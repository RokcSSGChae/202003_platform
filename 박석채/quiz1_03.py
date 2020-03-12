"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

input('주사위를 던지시겠습니까? ENTER')
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

if dice_1 > dice_2:
    winner = "첫번째 사람이 이겼습니다."
elif dice_1 == dice_2:
    winner = "비겼습니다."
else: winner = "두번째 사람이 이겼습니다."

print('첫번째 주사위 눈은 {}, 두번째 주사위 눈은 {}로 {}'.format(dice_1, dice_2, winner))