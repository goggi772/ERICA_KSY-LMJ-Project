import random
def fresh_deck():
    #player_deck_input함수를 이용해 플레이어가 원하는 카드개수를 선택한다.(20장 or 40장)
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
        suits= ['♠','♣','♥','◆']
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
            player_input = int(input('*원하시는 카드의 개수를 입력해주세요. (20 또는 40) :'))
            while not (player_input == 20 or player_input == 40):
                print("*20 또는 40 으로 다시 입력해주세요.")
                player_input = int(input('*원하시는 카드의 개수를 입력해주세요. (20 또는 40) :'))
            return player_input
        except ValueError:
            print("*자연수로 입력해주세요.")
            continue
