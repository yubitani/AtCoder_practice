#入力
marbles = input()

#計算
marbles_num = 0
for s in marbles:
    if s == "1":
        marbles_num += 1

#出力
print(marbles_num)