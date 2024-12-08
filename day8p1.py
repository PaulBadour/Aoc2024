from aoclib import *
DAY = 8
PART = 1

pInp = get_input(DAY)
ans = 0

freqs = {}
points = set()

for inum, i in enumerate(pInp):
    for jnum, j in enumerate(i):
        if j != "." and j not in freqs.keys():
            freqs[j] = [(inum, jnum)]
        elif j != ".":
            freqs[j].append((inum, jnum))

for key, val in freqs.items():
    for i in range(len(val) - 1):
        for j in range(i + 1, len(val)):
            v1, v2 = val[i], val[j]
            si = v2[0] - v1[0]
            sj = v2[1] - v1[1]
            p1 = (v1[0] + si, v1[1] + sj) if (v1[0] + si, v1[1] + sj) not in (v1, v2) else (v2[0] + si, v2[1] + sj)
            p2 = (v1[0] - si, v1[1] - sj) if (v1[0] - si, v1[1] - sj) not in (v1, v2) else (v2[0] - si, v2[1] - sj)
            if p1[0] < len(pInp) and p1[0] >= 0 and p1[1] < len(pInp[0]) and p1[1] >= 0:
                points.add(p1)
            if p2[0] < len(pInp) and p2[0] >= 0 and p2[1] < len(pInp[0]) and p2[1] >= 0:
                points.add(p2)

ans = len(points)
submit(DAY, PART, ans)