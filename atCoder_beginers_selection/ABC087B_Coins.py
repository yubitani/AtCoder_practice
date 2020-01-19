#入力
A = int(input())
B = int(input())
C = int(input())
X = int(input())

#合計金額をちょうどX円とする場合の数
ans = 0

#演算
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            total = 500 * i + 100 * j + 50 * k
            if total == X:
                ans += 1
                break

#出力
print(ans)