#入力
N, Y = map(int, input().split())

match_flag = False

# i: 10,000円札の枚数
for i in range(N+1):
    if match_flag:
        break
    # j: 5,000円札の枚数
    for j in range(N+1-i):
        # k: 1,000円札の枚数
        k = N - i - j
        otoshidama = 10000 * i + 5000 * j + 1000 * k
        if otoshidama == Y:
            print("{} {} {}".format(i, j, k))
            match_flag = True
            break

if not match_flag:
    print("-1 -1 -1")