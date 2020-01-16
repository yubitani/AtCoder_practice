import random


class quick_sorter:

    def __init__(self):

        self.query_ctr = 0

    def quick_sort(self, lst):
        """
        :param lst: a list you want to sort
        :return: null
        """
        #lstの中身が空の場合、以降の処理を実施せずreturn
        if not lst:
            return

        left = []
        right = []

        pivot = lst.pop()

        #分割
        while lst:
            e = lst.pop()


            if e < pivot:
                left.append(e)
            else:
                right.append(e)

            self.query_ctr += 1

        #再帰処理によるソート
        self.quick_sort(left)
        self.quick_sort(right)

        #結合
        left.reverse()
        while left:
            lst.append(left.pop())
        right.reverse()
        lst.append(pivot)
        while right:
            lst.append(right.pop())


# ボール数、クエリ数を取得

N = int(input())

# ソート対象のボールのリスト
balls = [chr(i) for i in range(65, 65 + N)]
random.shuffle(balls)

q = quick_sorter()
q.quick_sort(balls)
print("! {}".format("".join(balls)), flush=True)
print(q.query_ctr)
