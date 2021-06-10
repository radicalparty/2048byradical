import random, time
def merging(direct, mapping, n):#밀기
    mpg = mapping.copy()
    visit = [[False for _ in range(n)] for _ in range(n)]
    score = 0
    if direct == 1:#left
        for i in range(0, n):
            for j in range(0, n - 1):
                cnt = 0
                while True:
                    if cnt > n:
                        break
                    if mpg[i][j] == 0:
                        for k in range(j, n - 1):
                            mpg[i][k] = mpg[i][k + 1]
                            mpg[i][k + 1] = 0
                        cnt += 1
                    elif mpg[i][j] == mpg[i][j + 1] and visit[i][j] == False:
                        mpg[i][j] *= 2
                        score += mpg[i][j]
                        visit[i][j] = True
                        for k in range(j + 1, n - 1):
                            mpg[i][k] = mpg[i][k + 1]
                            mpg[i][k + 1] = 0
                        cnt += 1
                    elif mpg[i][j + 1] == 0:
                        for k in range(j + 1, n - 1):
                            mpg[i][k] = mpg[i][k + 1]
                            mpg[i][k + 1] = 0
                        cnt += 1
                    else:
                        break
    elif direct == 2:#right
        for i in range(0, n):
            for j in range(n - 1, 0, -1):
                cnt = 0
                while True:
                    if cnt > n:
                        break
                    if mpg[i][j] == 0:
                        for k in range(j, 0, -1):
                            mpg[i][k] = mpg[i][k - 1]
                            mpg[i][k - 1] = 0
                        cnt += 1
                    elif mpg[i][j - 1] == 0:
                        for k in range(j - 1, 0, -1):
                            mpg[i][k] = mpg[i][k - 1]
                            mpg[i][k - 1] = 0
                        cnt += 1
                    elif mpg[i][j] == mpg[i][j - 1] and (visit[i][j] == False):
                        mpg[i][j] *= 2
                        score += mpg[i][j]
                        visit[i][j] = True
                        for k in range(j - 1, 0, -1):
                            mpg[i][k] = mpg[i][k - 1]
                            mpg[i][k - 1] = 0
                        cnt += 1
                    else:
                        break
    elif direct == 3:#up
        for x in range(0, n):
            for y in range(0, n - 1):
                cnt = 0
                while True:
                    if cnt > n:
                        break
                    if mpg[y][x] == 0:
                        for k in range(y, n - 1):
                            mpg[k][x] = mpg[k + 1][x]
                            mpg[k + 1][x] = 0#1
                        cnt += 1
                    elif mpg[y][x] == mpg[y + 1][x] and visit[y][x] == False:
                        visit[y][x] = True
                        mpg[y][x] *= 2
                        score += mpg[y][x]
                        for k in range(y + 1, n - 1):
                            mpg[k][x] = mpg[k + 1][x]
                            mpg[k + 1][x] = 0#2
                        cnt += 1
                    elif mpg[y + 1][x] == 0:
                        for k in range(y + 1, n - 1):
                            mpg[k][x] = mpg[k + 1][x]
                            mpg[k + 1][x] = 0#3
                        cnt += 1
                    else:
                        break
    else:#down
        for x in range(0, n):
            for y in range(n - 1, 0, -1):
                cnt = 0
                while True:
                    if cnt > n:
                        break
                    if mpg[y][x] == 0:
                        for k in range(y, 0, -1):
                            mpg[k][x] = mpg[k - 1][x]
                            mpg[k - 1][x] = 0
                        cnt += 1
                    elif mpg[y - 1][x] == 0:
                        for k in range(y - 1, 0, -1):
                            mpg[k][x] = mpg[k - 1][x]
                            mpg[k - 1][x] = 0
                        cnt += 1
                    elif mpg[y - 1][x] == mpg[y][x] and visit[y][x] == False:
                        visit[y][x] = True
                        mpg[y][x] *= 2
                        score += mpg[y][x]
                        for k in range(y - 1, 0, -1):
                            mpg[k][x] = mpg[k - 1][x]
                            mpg[k - 1][x] = 0
                        cnt += 1
                    else:
                        break
    return mpg, direct, score
def mapmaker(n):
    mpg = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    while cnt < 2:
        r1 = random.randrange(0, n)
        r2 = random.randrange(0, n)
        if mpg[r1][r2]:
            continue
        k = random.randrange(0, 5)
        mpg[r1][r2] = (4 if k % 5 == 1 else 2)
        cnt += 1
    return mpg
def blockset(mapping, n, set3):
    mpg = mapping.copy()
    while True:
        x = random.randrange(0, n)
        y = random.randrange(0, n)
        if mpg[x][y]:
            continue
        if set3:
            k = random.randrange(1, 15)
            k = k - 7
            if k <= 0:
                k = 1
            mpg[x][y] = pow(2, k)
        else:
            k = random.randrange(0, 5)
            mpg[x][y] = (4 if k % 5 == 1 else 2)
        break
    return mpg
def cntmax(mapping, n):#게임종료 조건에 충족 => 게임종료
    mpg = mapping.copy()
    usedlr = [[False for _ in range(n)] for _ in range(n)]
    usedud = [[False for _ in range(n)] for _ in range(n)]
    ck = True
    cntlr = cntud = 0
    for i in range(n):
        for j in range(n):
            if mpg[i][j] == 0:
                ck = False
            if j == n - 1:
                continue
            elif usedlr[i][j] or usedlr[i][j + 1]:
                continue
            if mpg[i][j] == mpg[i][j + 1]:
                cntlr += 1
                usedlr[i][j] = usedlr[i][j + 1] = True
    for i in range(n):
        for j in range(n):
            if i == n - 1:
                continue
            elif usedud[i][j] or usedlr[i + 1][j]:
                continue
            if mpg[i][j] == mpg[i + 1][j]:
                cntud += 1
                usedud[i][j] = usedud[i + 1][j] = True
    if cntlr == cntud == 0 and ck:
        return True
    else:
        return False
def rule(mode):
    string = ("boss" if mode == 2 else "normal")
    print("일단 룰을 설명하기 전에 게임을 플레이해주셔서 감사합니다.\n")
    time.sleep(3)
    print("이 게임은 2048이라는 게임이 원본으로, 수들끼리 상하좌우로 합치면서 점수를 많이 얻으면 승리합니다.\n")
    time.sleep(3)
    print("합칠 때 상하좌우에 있는 같은 수 끼리 합칠 수 있으며, 만약 한 방향으로 밀면 다른 블록도 같이 밀립니다\n")
    time.sleep(3)
    print("재밌게 플레이 해주세요!")
    time.sleep(2)
    return
def setting(set1, set2, set3):
    while True:
        print("-----------------------------------------------")
        print("                      설정                     ")
        print("   (1) 스코어에 턴 수 반영 : {}    ".format("ON" if set1 else "OFF"))
        print("   (2) 세 턴 이상 병합 안할시 게임 종료 : {}".format("ON" if set2 else "OFF"))
        print("   (3) 랜덤 생성 블록에 랜덤 숫자 : {}".format("ON" if set3 else "OFF"))
        print()
        print("-----------------------------------------------")
        print()
        try:
            x = int(input("변경할 설정 선택, 설정 변경 그만하고 싶으면 다른 숫자 입력"))
            if x == 1:
                set1 = not set1
            elif x == 2:
                set2 = not set2
            elif x == 3:
                set3 = not set3
            else:
                break
        except:
            print("다시 입력")
        
        
    return set1, set2, set3
def button():
    print("------------------------------------------------------------------")
    print("|            이 게임을 플레이 해 주셔서 감사합니다               |")
    time.sleep(2)
    print("|                                                                |")
    print("|                                                                |")
    print("|                           2048                                 |")
    print("|                                                                |")
    print("|                         난이도                                 |")
    print("|                         상: 3, 4                               |")
    print("|                         중: 5                                  |")
    print("|                         하: 6, 7, 8                            |")
    print("|                                                                |")
    print("|                         설정 : 5252                            |")
    time.sleep(2)
    print("|                                                                |")
    time.sleep(2)
    print("|                        게임 종료: 9999                         |") 
    print("------------------------------------------------------------------")
