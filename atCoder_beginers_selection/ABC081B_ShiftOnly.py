#入力
n = int(input())
numList = [a for a in map(int,input().split())]

#変数定義
divide_ctr = 0 #2で割れた回数
divide_flg = True

#計算
while divide_flg:
    for i in range(n):
        if numList[i] % 2 == 0:
            numList[i] /= 2
        else:
            divide_flg = False
            break
    if divide_flg:
        divide_ctr += 1


#出力
print(divide_ctr)
