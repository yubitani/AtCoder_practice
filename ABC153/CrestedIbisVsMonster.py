#入力
H, N = map(int, input().split())
A = []
B = []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[h]: 敵のHPをh減らすために必要な最小の魔力
dp = [0]
# min_hp: 敵のHPをh減らすために必要な最小の魔力（暫定）
for h in range(1, H+1):
    min_mp = dp[max(h - A[0],0)] + B[0]
    for n in range(1, N):
        min_mp = min(min_mp, dp[max(h - A[n],0)] + B[n])
    dp.append(min_mp)

#出力
print(dp[H])