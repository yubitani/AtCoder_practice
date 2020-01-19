#入力
N, A, B = map(int, input().split())

class Number:
    def __init__(self, num):
        self.num = num
        self.digit_sum = self.calc_digit_sum()
    def calc_digit_sum(self):
        res = 0
        for c in str(self.num):
            res += int(c)
        return res

#1以上N以下のNumberオブジェクトの作成
numbers = []
for n in range(1,N+1):
    numbers.append(Number(n))

#10進数の各桁の和がA以上B以下のNumberオブジェクトを選定
matched_numbers = list(filter(lambda x: A <= x.digit_sum <= B, numbers))

#該当するNumberの総和
total = 0
for number in matched_numbers:
    total += number.num

#出力
print(total)