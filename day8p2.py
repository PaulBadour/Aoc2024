from aoclib import *
DAY = 8
PART = 2

pInp = get_input(DAY)
ans = 0

freqs = {}
points = set()

for inum, i in enumerate(pInp):
    for jnum, j in enumerate(i):
        if j != "." and j not in freqs.keys() and j != '#':
            freqs[j] = [(inum, jnum)]
        elif j != "." and j != '#':
            freqs[j].append((inum, jnum))

for key, val in freqs.items():
    for i in range(len(val) - 1):
        for j in range(i + 1, len(val)):
            v1, v2 = val[i], val[j]
            si = v2[0] - v1[0]
            sj = v2[1] - v1[1]
            good = True
            p1, p2 = v1, v2
            p1dir = 1 if (p1[0] + si, p1[1] + sj) != p2 else -1
            while good:
                p1 = (p1[0] + (si * p1dir), p1[1] + (sj * p1dir))
                if p1[0] < len(pInp) and p1[0] >= 0 and p1[1] < len(pInp[0]) and p1[1] >= 0:
                    points.add(p1)
                else:
                    good = False

            good = True
            p1dir *= -1
            while good:
                p2 = (p2[0] + (si * p1dir), p2[1] + (sj * p1dir))
                if p2[0] < len(pInp) and p2[0] >= 0 and p2[1] < len(pInp[0]) and p2[1] >= 0:
                    points.add(p2)
                else:
                    good = False
                
                
# p2 = (p1[0] - si, p1[1] - sj) if (p1[0] - si, p1[1] - sj) not in (p1, p2) else (p2[0] - si, p2[1] - sj)
for i in freqs.values():
    for j in i:
        points.add(j)
ans = len(points)
for i in points:
    print(i)
submit(DAY, PART, ans)