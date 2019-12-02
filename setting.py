import random
import time
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
        time.sleep(1.1)
        present = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]
        return deck, present

