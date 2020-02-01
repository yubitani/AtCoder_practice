N = int(input())
listHop = []
for i in range(N):
    t, x, y = map(int, input().split())
    listHop.append((t, x, y))

flag = True

hop1 = (0, 0, 0)
for hop2 in listHop:
    hop_diff = [hop2[i] - hop1[i] for i in range(3)]
    distance = hop_diff[1] + hop_diff[2]
    if hop_diff[0] < distance or hop_diff[0] % 2 != distance % 2:
        flag = False
        break
    else:
        hop1 = hop2

if flag:
    print("Yes")
else:
    print("No")