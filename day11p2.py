from aoclib import *
from functools import cache
DAY = 11
PART = 2

pInp = get_input(DAY)
ans = 0

@cache
def splits(num, n):
    if n == 75:
        return 1
    if num == 0:
        return splits(1, n+1)
    ln = len(str(num))
    if ln % 2 == 0:
        l,r = int(str(num)[:int(ln/2)]), int(str(num)[int(ln/2):])
        return splits(l, n+1) + splits(r, n+1)
    else:
        return splits(num*2024,n+1)

for i in getints(pInp[0]):
    print(i)
    ans += splits(i, 0)

submit(DAY, PART, ans)