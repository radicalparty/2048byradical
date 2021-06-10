import sys, function, random, time
#2048을 규칙으로 풀기 위한 도구
set1 = set2 = set3 = False
while True:
    print("난이도를 입력해 주세요: 난이도 & 기능에 대해 알고 싶다면 2021 입력")
    try:
        n = int(sys.stdin.readline())
        if n == 5252:
            set1, set2, set3 = function.setting(set1, set2, set3)
        elif n == 2021:
            function.button()
        elif n == 9999:
            exit()
        elif n >= 9 or n < 3:
            print("난이도가 존재하지 않습니다", end = "")
        else:
            break
    except:
        print("다시 입력해 주세요")
kesk = 0
function.rule(1)
mpg = function.mapmaker(n)
turn = 0
totalscore = 0
while True:
    if turn != 0:
        mpg = function.blockset(mpg, n, set3)
    turn += 1
    print("현재 점수 : {}".format(totalscore))
    print("---------------------")
    for i in range(n):
        for j in range(n):
            print(mpg[i][j], end = "   ")
        print()
    print("---------------------")
    print("\n\n")
    while True:
        print("밀 방향을 결정하세요: 왼쪽 : L/l, 오른쪽 : R/r, 위쪽 : U/u, 아래쪽: D/d")
        alphabet = sys.stdin.readline().rstrip("\n")
        if alphabet == "L" or alphabet == "l":
            direct = 1
            break
        elif alphabet == "R" or alphabet == "r":
            direct = 2
            break
        elif alphabet == "U" or alphabet == "u":
            direct = 3
            break
        elif alphabet == "D" or alphabet == "d":
            direct = 4
            break
        else:
            continue
    mpg, direct, score = function.merging(direct, mpg, n)
    if score == 0:
        kesk += 1
    else:
        kesk = 0
    if set2 and kesk >= 3:
        break
    totalscore += score
    if function.cntmax(mpg, n):
        break
if set1:
    totalscore += turn * 20
if set2:
    print("3턴 동안 병합을 하지 않아 패배 하였습니다.")
print("-----------------")
print("                 ")
print("                 ")
print("   Game Over     ")
print("                 ")
print("  총 점수: {}    ".format(totalscore))
print("                 ")
print("                 ")
print("                 ")
print("-----------------")
    
    

