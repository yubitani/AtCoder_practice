class quick_sorter:

    def __init__(self, query_ctr):
        """
        :param query_ctr: a number of times you can submit query
        """
        self.query_ctr = query_ctr

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

            print("? {} {}".format(pivot, e), flush=True)
            self.query_ctr -= 1

            if input() == ">":
                left.append(e)
            else:
                right.append(e)

            if self.query_ctr <= 0:
                raise

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

N, Q = map(int, input().split(" "))

# ソート対象のボールのリスト
balls = [chr(i) for i in range(65, 65 + N)]

try:
    q = quick_sorter(Q)
    q.quick_sort(balls)
    print("! {}".format("".join(balls)), flush=True)

#
except RuntimeError:
    print("Query_ctr exceeded the limit.")
