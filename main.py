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

    while deck != []:
        ro_und += 1
        # 카드 한장씩 나눠가짐.
        player_card = deck[0]
        deck = deck[1:]
        com_card = deck[0]
        deck = deck[1:]
        player_betting_chips = 0
        com_betting_chips = 0
        table_chips += 2 #기본 베팅금
        player_chips -= 1
        player_betting_chips += 1
        com_chips -= 1
        com_betting_chips += 1
        print("\n\n*자신의 카드를 이마 위에 붙여주세요.\n")
        time.sleep(0.5)
        print_table(ro_und, com_card, com_chips, player_chips, table_chips)
        player_betting_win = False
        com_betting_win = False

        player_value = player_card["rank"] if not player_card["rank"] == "A" else 1
        com_value = com_card["rank"] if not com_card["rank"] == "A" else 1
        present.remove(player_value)
        isAllIn = False
        while True:
            #베팅시작###############################################################################
            if player_turn:
                print("*플레이어님의 차례입니다. 베팅을 해주시지요.")
                response = playerBetting(com_betting_chips, player_betting_chips, player_chips)
                while player_chips < response and not response >= (com_betting_chips)-(player_betting_chips):
                    print("*보유 칩 개수보다 높은 숫자를 입력할 수 없습니다.")
                    response = playerBetting()
                table_chips += response
                player_chips -= response
                player_betting_chips += response
                print_table(ro_und, com_card, com_chips, player_chips, table_chips)
            
                print("●  플레이어님께서", response, "개의 칩을 베팅하셨습니다.", "\n●  플레이어님은 총", player_betting_chips, "개의 칩을 베팅하셨습니다.")
                print("○  컴퓨터는 총", com_betting_chips, "개 의 칩을 베팅했습니다.")
                time.sleep(1)
                if response == 0:
                    print("*플레이어님께서 다이를 하셨으므로 베팅은 컴퓨터의 승리로 종료되었습니다.\n")
                    #다이해서 끝
                    player_turn = False
                    com_turn = True
                    com_betting_win = True
                    break
                elif player_betting_chips == com_betting_chips:
                    print("*플레이어님과 컴퓨터의 베팅한 칩의 개수가 같아졌으므로 베팅을 종료합니다.\n")
                    #동률로 베팅 끝
                    player_turn = False
                    com_turn = True
                    break
                elif player_chips == 0:
                    isAllIn = True
                    if player_betting_chips < com_betting_chips:
                        #상대랑 같아지려면 칩수 부족해서 올인
                        print("*칩 수가 부족했지만, 플레이어님께서 올인을 함으로써 베팅이 종료되었습니다.\n")
                        player_turn = False
                        com_turn = True
                        break
                    else:
                        print("*플레이어님께서 올인을 하셨습니다.")
                player_turn = False
                com_turn = True
            elif com_turn:
                print("*컴퓨터 차례입니다.")
                print("*컴퓨터가 베팅을 하기를 기다려주세요.")
                time.sleep(1.5)
                if isAllIn:
                    isAllIn = False
                    if player_betting_chips-com_betting_chips > com_chips:
                        behavior = select_behavior(present, player_value, com_chips, com_chips) # 다이 or 올인
                    else:
                        behavior = select_behavior(present, player_value, (player_betting_chips)-(com_betting_chips), (player_betting_chips)-(com_betting_chips)) # 다이 or 격차만큼 베팅
                else:
                    if (player_betting_chips)-(com_betting_chips) >= com_chips: # 칩 부족:다이 or 올인
                        behavior = select_behavior(present, player_value, com_chips, com_chips) # 다이 or 올인
                    else:
                        if com_chips - (player_betting_chips-com_betting_chips) - player_chips >= 0: # 칩 많음:컴퓨터가 베팅에서 손해보지 않게 손봐줌. 최댓값의 경계값을 정해줌
                            behavior = select_behavior(present, player_value, (player_betting_chips)-(com_betting_chips), (player_betting_chips)-(com_betting_chips) + player_chips) #불필요한 베팅을 자제함.
                        else:
                            behavior = select_behavior(present, player_value, (player_betting_chips)-(com_betting_chips), com_chips)
                table_chips += behavior
                com_chips -= behavior
                com_betting_chips += behavior
                print_table(ro_und, com_card, com_chips, player_chips, table_chips)
                print("○  컴퓨터가", behavior, "개의 칩을 베팅했습니다.", "\n○  컴퓨터는 총", com_betting_chips, "개의 칩을 베팅했습니다.")
                print("●  플레이어님은 총", player_betting_chips, "개 의 칩을 베팅하셨습니다.")
                time.sleep(1)
                if behavior == 0:
                    print("*컴퓨터가 다이를 했으므로 베팅은 플레이어님의 승리로 종료되었습니다.\n")
                    #다이해서 끝
                    player_betting_win = True
                    player_turn = True
                    com_turn = False
                    break
                elif player_betting_chips == com_betting_chips:
                    print("*컴퓨터의 베팅한 칩의 개수가 플레이어님과 같아졌으므로 베팅을 종료합니다.\n")
                    #동률로 베팅 끝
                    player_turn = True
                    com_turn = False
                    break
                elif com_chips == 0:
                    if player_betting_chips > com_betting_chips:
                        #상대랑 같아지려면 칩수 부족해서 올인
                        print("*칩 수가 부족했지만, 컴퓨터가 올인을 함으로써 베팅이 종료되었습니다.\n")
                        player_turn = True
                        com_turn = False
                        break
                    else:
                        print("*컴퓨터가 올인을 했습니다.")
                player_turn = True
                com_turn = False
        #베팅끝###############################################################################
        #베팅결과가지고 칩나눠갖고
        present.remove(com_value)
        time.sleep(0.5)
        print("*카드를 공개하겠습니다!")
        time.sleep(0.7)
        print("* 플레이어", player_card["suit"]+" "+str(player_card["rank"]), "vs", "컴퓨터", com_card["suit"]+" "+str(com_card["rank"]),"*")
        if com_betting_win:
            time.sleep(0.5)
            print("*플레이어님은 칩", player_betting_chips, "개를 잃으셨고, 컴퓨터는 칩", table_chips-com_betting_chips, "개를 얻었습니다.\n")
            time.sleep(0.5)
            if player_value == 10: #패널티
                print("*플레이어님께서 10 을 든 상태로 '다이'를 외쳤으므로 칩 10개라는 패널티를 주겠습니다.\n")
                time.sleep(0.5)
                player_chips -= 10
                com_chips += 10
            com_chips += table_chips
            table_chips = 0
        elif player_betting_win:
            time.sleep(0.5)
            print("*플레이어님은 칩", table_chips-player_betting_chips, "개를 얻으셨고, 컴퓨터는 칩", com_betting_chips, "개를 잃었습니다.\n")
            time.sleep(0.5)
            if com_value == 10: #패널티
                print("*컴퓨터는 10 을 든 상태로 '다이'를 외쳤으므로 칩 10개 패널티를 주겠습니다.\n")
                time.sleep(0.5)
                com_chips -= 10
                player_chips += 10
            player_chips += table_chips
            table_chips = 0
        elif player_value > com_value:
            time.sleep(0.5)
            print("*숫자 비교를 해보았을 때, 플레이어님이", ro_und, "라운드에서 승리하셨습니다.")
            time.sleep(0.5)
            print("*플레이어님은 칩", table_chips-player_betting_chips, "개를 얻으셨고, 컴퓨터는 칩", com_betting_chips, "개를 잃었습니다.\n")
            time.sleep(0.5)
            player_chips += table_chips
            table_chips = 0
        elif player_value < com_value:
            print("*숫자 비교를 해보았을 때, 컴퓨터가", ro_und, "라운드에서 승리했습니다.")
            print("*플레이어님은 칩", player_betting_chips, "개를 잃으셨고, 컴퓨터는 칩", table_chips-com_betting_chips, "개를 얻었습니다.\n")
            time.sleep(0.5)
            com_chips += table_chips
            table_chips = 0
            time.sleep(0.5)
        else:#숫자가 같을때
            print("*숫자가 같네요. 비겼습니다. 테이블 위의 베팅된 칩은 그대로 두고 다음 라운드 진행하겠습니다.\n")
            time.sleep(0.5)
        if not (player_chips-1 > 0 and com_chips-1 > 0):
            break
        while not more("*다음 라운드를 시작하시겠습니까? (y/n) : "):
            print("*준비되시면 y 를 입력해주시길 바랍니다.")
            pass

    if not (player_chips-1 > 0 and com_chips-1 > 0):
        if (player_chips-1) == (com_chips-1):
            print("*양쪽 플레이어의 칩 부족으로 더 이상 게임 진행이 불가능한 상태입니다.\n*최종승패를 가르도록 하겠습니다.\n")
            print("!인디언포커 무승부! <플레이어 칩 개수 : ", player_chips, "개", " vs ", "컴퓨터 칩 개수 : ", com_chips, "개>\n",sep='')
            time.sleep(1)
        if not (player_chips-1) > 0:
            print("*플레이어님의 칩 부족으로 더 이상 게임 진행이 불가능한 상태입니다.\n*최종승패를 가르도록 하겠습니다.\n")
            time.sleep(1)
            print("!컴퓨터 인디언포커 최종승리! < 컴퓨터 칩 개수 : ", com_chips, "개", " vs ", "플레이어 칩 개수 : ",player_chips, "개\n(음수는 빚진 것 입니다.)\n",sep='')
            time.sleep(0.5)
        elif not (com_chips-1) > 0:
            print("*컴퓨터의 칩 부족으로 더 이상 게임 진행이 불가능한 상태입니다.\n*최종승패를 가르도록 하겠습니다.\n")
            time.sleep(1)
            print("!플레이어 인디언포커 최종승리! <플레이어 칩 개수 : ", player_chips, "개", " vs ", "컴퓨터 칩 개수 : ", com_chips, "개>\n(음수는 빚진 것 입니다.)\n",sep='')
            time.sleep(0.5)
    else:
        print("*덱이  모두 소진된 이유로 칩의 개수에 근거하여 최종 승패를 가리도록 하겠습니다.\n")
        time.sleep(1)
        if com_chips > player_chips:
            print("!컴퓨터 인디언포커 최종승리! < 컴퓨터 칩 개수 : ", com_chips, "개", " vs ", "플레이어 칩 개수 : ",player_chips, "개\n",sep='')
        elif com_chips < player_chips:
            print("!플레이어 인디언포커 최종승리! <플레이어 칩 개수 : ", player_chips, "개", " vs ", "컴퓨터 칩 개수 : ", com_chips, "개>\n",sep='')
        else:
            print("!인디언포커 무승부! <플레이어 칩 개수 : ", player_chips, "개", " vs ", "컴퓨터 칩 개수 : ", com_chips, "개>\n",sep='')
        time.sleep(0.5)
    #more
    if more("*게임을 한 판 더 하겠습니까? (y/n) : "):
        print("*새 게임 세트를 준비합니다.\n")
        time.sleep(1)
        print("*새 게임을 시작합니다.\n")
        indianFoker()
    else:
        print("*게임을 종료합니다")

indianFoker()
            
