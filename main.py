from setting import *
from print_table import *
from calculator import *
import random
import time

def indianFoker():
    deck, present = fresh_deck()
    player_card = None
    com_card = None
    player_turn = False
    com_turn = False
    player_chips = 30
    com_chips = 30
    print("*순서를 정하는 중입니다.")
    time.sleep(0.5)
    if random.randint(0, 1) == 0: #선 정하기
        player_turn = True
        print("\n\n*플레이어님이 선플레이어 입니다.")
    else:
        com_turn = True
        print("\n\n*컴퓨터가 선플레이어 입니다.")
    ro_und = 0

    table_chips = 0


