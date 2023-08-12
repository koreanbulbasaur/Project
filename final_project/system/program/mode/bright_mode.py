import screen_brightness_control as sbc
import random

def bright_program(num):
    # 현재 화면 모니터 밝기
    current_brightness = sbc.get_brightness()

    brightness_level = level(current_brightness, num)

    sbc.set_brightness(brightness_level)
    random_n = random.randint(0, 100)

    # 확률로 짠으로 출력함
    if 100 == random_n:
        return '짠!'

    text = f"화면 밝기를 {brightness_level}으로 조절해드렸습니다."
    return text

# 화면 밝기 계산
def level(curr_n, n):

    # 최대
    if n in 'maximum':
        output_level = 100

    # 중간
    elif n in 'medium' or n in 'mid':
        output_level = 50

    # 조금 밝게
    elif n in 'slightly brighter':
        output_level = curr_n + 10

    # 어둡게
    elif n in 'dim':
        output_level = 0

    else:
        output_level = int(n)

    # 최대 밝기 100, 최소 밝기 0
    if output_level >= 100:
        output_level = 100
    elif output_level <= 0:
        output_level = 0

    return output_level