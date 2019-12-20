def playerBetting(com_betting_chips, player_betting_chips, maxChips):
    while True:
        try:
            player_betting = input('*베팅하실 칩의 개수를 적어주세요. (\'Die\' = 0) : ')
            if not player_betting.isdecimal():
                print("*'0' 또는 정수로 입력해주세요.")
                continue
            if not com_betting_chips == 1:
                if not ((com_betting_chips)-(player_betting_chips) <= int(player_betting) <= maxChips\
                        or int(player_betting) == 0):
                    print("*베팅의 선택지는", "\n-1 \'다이\' (\'0\')\n-2 최솟값은 ((컴퓨터 베팅한 칩의 수) - (플레이어 베팅한 칩의 수))\n-3 최댓값은 플레이어 보유 칩 개수\n-4 올인 (베팅을 하고 싶지만 2번 성립이 \
불가능 할 때)\n*뿐 입니다. 잘 선택해주세요.")
                    continue
            return int(player_betting)
        except ValueError:
            print("*'0' 또는 정수로 입력해주세요.")
            continue

def more(message):
    result = input(message)
    if result == 'y' or result == 'Y':
        return True
    elif result == 'n' or result == 'N':
        return False
    else:
        print("*입력이 잘못되었습니다. 다시 한번 입력해주세요.")
        return more(message)
    
import random
def fresh_deck():
    if player_deck_input() == 40:
        suits = {'♠','♣','♥','◆'}
        ranks = {'A', 2, 3, 4, 5, 6, 7, 8, 9, 10}
        deck = []
        for i in suits:
            for k in ranks:
                deck.append({"suit":i, "rank":k})
        random.shuffle(deck)
        print("*카드를 섞는 중입니다...")
        import time
        time.sleep(1.1)
        present = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]
        return deck, present
    else:
        suits = ['♠','♣','♥','◆']
        ranks = ['A','A',2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        deck = []
        for i in ranks:
            deck.append({"suit":random.choice(suits), "rank":i})
        random.shuffle(deck)
        print("*카드를 섞는 중입니다...")
        import time
        time.sleep(1.1)
        present = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        return deck, present

def player_deck_input():
    while True:
        try:
            player_input = int(input('*원하시는 카드의 개수를 입력해주세요. (20 또는 40) : '))
            while not (player_input == 20 or player_input == 40):
                print("*20 또는 40 으로 다시 입력해주세요.")
                player_input = int(input('*원하시는 카드의 개수를 입력해주세요. (20 또는 40) : '))
            if player_input == 20:
                return player_input
            elif player_input == 40:
                return player_input
        except ValueError:
            print("*자연수로 입력해주세요.")
            continue
