import random
import time
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
        time.sleep(1.1)
        present = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]
        return deck, present
    else:
        suit = ['♠','♣','♥','◆']
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
    while
