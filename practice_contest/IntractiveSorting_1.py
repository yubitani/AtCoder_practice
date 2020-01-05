#アルファベットのリストを作成
alphabets = [chr(i) for i in range(65, 65+26)]

#ボール数、クエリ数を取得
N,Q = map(int,input().split(" "))

#ソート結果
balls = alphabets[0:N]

#クエリ回数の残
query_ctr = Q

#ボールの並び替え
for i in range(N):
    for j in range(i+1,N):

        #比較対象のボールの文字とそのボールの現時点の並び順を変数に代入
        c1 = alphabets[i]
        c1_index = balls.index(c1)
        c2 = alphabets[j]
        c2_index = balls.index(c2)

        #クエリの発行
        print("? {} {}".format(c1, c2), flush=True)
        ans = input()
        query_ctr -= 1

        #c1がc2より重い場合、順番を入れ替え
        if ans == ">":
            balls[c1_index] = c2
            balls[c2_index] = c1

        #クエリ回数の残がゼロとなったらbreak
        if query_ctr <= 0:
            break

#ソート結果の出力
print("! {}".format("".join(balls)), flush=True)
