def select_behavior(present,opponentNum,minChips,maxChips):
    average = int(sum(present) / len(present)) #덱에 남은 카드들 평균
    weight  = abs(average - opponentNum)  #가중치
    length = maxChips - minChips + 2 #다이의 경우의수포함
    p = 100 / length
    arr = []
    for i in range(length):
        arr.append(p)


