#入力
N = int(input())
list_A = list(map(int, input().split()))

#昇順にソート
list_A.sort()

#各合計を算出
sum_of_Alice = 0
sum_of_Bob = 0
for i in range(N):
    if i % 2 == 0:
        sum_of_Alice += list_A.pop()
    else:
        sum_of_Bob += list_A.pop()

#結果の出力
result = sum_of_Alice - sum_of_Bob
print(result)