#ボール数、クエリ数を取得
import random

N,Q = map(int,input().split(" "))

#ソート結果
balls = [chr(i) for i in range(65, 65 + N)]

#クエリ回数の残
query_ctr = Q

def quick_sort(arr, start, end):
    left = []
    right = []
    if len(arr) < 2:
        print(arr)
        return arr

    pivot = start + int((end + 1 - start) / 2.0)

    for i in range(start, end + 1):
        if i == pivot:
            continue
        else:
            print("? {} {}".format(arr[pivot], arr[i]), flush=True)
            if input() == ">":
                left.append(arr[i])
            else:
                right.append(arr[i])

    left = quick_sort(left, start, pivot)
    right = quick_sort(right, pivot + 1, end)
    cat_list = []
    cat_list.extend(left)
    cat_list.append(arr[pivot])
    cat_list.extend(right)

    return cat_list

balls = quick_sort(balls, 0, N-1)
print("! {}".format("".join(balls)), flush=True)
