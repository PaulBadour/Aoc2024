from aoclib import *
DAY = 1
PART = 1

pInp = get_input(DAY)
ans = 0

l1 = []
l2 = []


# Code

for i in pInp:
    n1, n2 = i[:5], i[-5:]
    n1 = int(n1)
    n2 = int(n2)

    l1.append(n1)
    l2.append(n2)

l1 = sorted(l1)
l2 = sorted(l2)
for i in range(len(l1)):
    ans += abs(l1[i] -l2[i])

submit(DAY, PART, ans)