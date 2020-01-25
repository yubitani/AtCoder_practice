#入力
N = int(input())
list_d = []
for i in range(N):
    list_d.append(int(input()))

#ソート
list_d = list(set(list_d))
#重複排除
list_d.sort()

#出力
print(len(list_d))