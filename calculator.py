import random
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
    weight += 1 / len(arr)*30 # 일단 임의설정
    
    if average > opponentNum or opponentNum == 10: #자신있을때 / 블러핑의경우포함
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
            if random.randint(1,10) > 3: # 70%로저돌적 행동/테스트후 수정가능성
                arr[length - 1] += arr[0]
                arr[0] = 0
            else:
                arr[length - 1] += arr[0]/2
                arr[0] /= 2
    elif average < opponentNum:#자신없을때
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
        return random.randint(minChips,maxChips)
    if average > opponentNum:
        behavior = arrSelect(arr,weight,True)
    else:
        behavior = arrSelect(arr,weight,False)
    if minChips == 0:
        return behavior
    else:
        if behavior == 0:
            return 0
        else:
            return behavior + minChips - 1


def arrSelect(arr,weight,advantage): #배열에서 원소선택기
    randomWeight = weight * 5 #임의설정 테스트후 수정
    if advantage:
        if randomWeight > 100:
            a = 100
        else:
            a = random.randint(int(randomWeight),100)
        b = 0
        for i in arr:
            b += i
            if b >= a:
                return arr.index(i)
    else:
        if randomWeight > 100:
            a = 0
        else:
            a = random.randint(0,int(100 - randomWeight))
        b = 0
        for i in arr:
            b += i
            if b >= a:
                return arr.index(i)




