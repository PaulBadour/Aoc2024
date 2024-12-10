from aoclib import *
DAY = 10
PART = 2

pInp = get_input(DAY)
ans = 0

th = set()
cur = set()

def dive(point):
    num = pInp[point[0]][point[1]]
    if num == 9:
        return 1
    res = 0
    if point[0] > 0 and pInp[point[0] - 1][point[1]] == num + 1:
        res += dive((point[0] - 1, point[1]))

    if point[1] > 0 and pInp[point[0]][point[1] - 1] == num + 1:
        res += dive((point[0], point[1] - 1))

    if point[0] < len(pInp) - 1 and pInp[point[0] + 1][point[1]] == num + 1:
        res += dive((point[0] + 1, point[1]))

    if point[1] < len(pInp[0]) - 1 and pInp[point[0]][point[1] + 1] == num + 1:
        res += dive((point[0], point[1] + 1))

    return res

for i in range(len(pInp)):
    pInp[i] = list(map(lambda x: int(x), list(pInp[i])))
    for j in range(len(pInp[i])):
        if pInp[i][j] == 0:
            th.add((i, j))

for i in th:
    cur = set()
    ans += dive(i)




submit(DAY, PART, ans)