N, K = map(int, input().split())
monsterList = [int(x) for x in input().split()]

atackTimes = 0

monsterList.sort()
if K != 0:
    for hp in monsterList[:-K]:
        atackTimes += hp
else:
    for hp in monsterList:
        atackTimes += hp

print(atackTimes)