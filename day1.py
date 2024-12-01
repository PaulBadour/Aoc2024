from aoclib import *
DAY = 1
PART = 2

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
# l2 = sorted(l2)
for i in range(len(l1)):
    ans += l1[i] * l2.count(l1[i])

submit(DAY, PART, ans)