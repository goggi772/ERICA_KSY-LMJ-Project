def select_behavior(present,opponentNum,minChips,maxChips):
    average = int(sum(present) / len(present)) #덱에 남은 카드들 평균
    weight  = abs(average - opponentNum)  #가중치
    if minChips == 0:
        length = (maxChips - minChips) + 1
    else:
        length = maxChips - minChips + 2 #다이의 경우의수포함
    p = 100 / length
    arr = []
    for i in range(length):
        arr.append(p)
    weight += 1 / len(arr)*30
    
    if average > opponetNum or opponetNum == 10: #자신있을때 / 블러핑의경우포함
        if length%2 == 0:
            k = 1
            for i in range(length//2,length):
                arr[i] += weight * k
                arr[-i-1] -= weight * k
                k += 1
        else: #리스트길이 홀수
            k = 1
            for i in range(length//2 + 1,length):
                arr[i] += weight * k
                arr[-i-1] -= weight * k
                k += 1
        if opponentNum == 10:
            if random.randint(1,10) > 3: # 70% 로 저돌적행동
                arr[length - 1] += arr[0]
                arr[0] = 0
            else:
                arr[length - 1] += arr[0]/2
                arr[0] /= 2
    elif average < opponetNum:#자신없을때
        if length%2 == 0:
            k = 1
            for i in range(length//2,length):
                arr[i] -= weight * k
                arr[-i-1] += weight * k
                k += 1
        else: #리스트길이 홀수
            k = 1
            for i in range(length//2 + 1,length):
                arr[i] -= weight * k
                arr[-i-1] += weight * k
                k += 1

    else: #average == opponentNum 가중치사용안할때




