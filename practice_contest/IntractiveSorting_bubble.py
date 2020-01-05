#ボール数、クエリ数を取得
N,Q = map(int,input().split(" "))

#ソート結果
balls = [chr(i) for i in range(65, 65 + N)]

#クエリ回数の残
query_ctr = Q

#ボールの並び替え

change = True
while change:
    change = False
    for i in range(N - 1):
        c1 = balls[i]
        c2 = balls[i+1]
        #クエリの発行
        print("? {} {}".format(balls[i], balls[i+1]), flush=True)
        ans = input()
        query_ctr -= 1

        #c1がc2より重い場合、順番を入れ替え
        if ans == ">":
            balls[i], balls[i+1] = c2, c1
            change = True

        #クエリ回数の残がゼロとなったらbreak
        if query_ctr <= 0:
            break

#ソート結果の出力
print("! {}".format("".join(balls)), flush=True)
