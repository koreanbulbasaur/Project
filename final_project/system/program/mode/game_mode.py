import random
from playsound import playsound

def game_dice():
    i = random.randint(1, 6)
    playsound('./program/mode/game/dice_roll.wav')
    if i in [1, 3, 6]:
        return f'{i}이 나왔습니다.'
    else:
        return f'{i}가 나왔습니다.'

def choose_number(first_n, last_n):
    i = random.randint(first_n, last_n)
    playsound('./program/mode/game/choose_n.wav')
    return f'{i}'

def game_coin():
    coin = ['앞면', '뒷면']
    playsound('./program/mode/game/coin.wav')
    coin_choice = random.choice(coin)
    return f'{coin_choice}이 나왔습니다.'

def game_program(game, number=None):
    if game == 'dice':
        output_text = game_dice()
    elif game == 'choose':
        first_n, last_n = map(int, number.split('-'))
        output_text = choose_number(first_n, last_n)
    elif game == 'coin':
        output_text = game_coin()

    return output_text