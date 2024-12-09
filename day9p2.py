from aoclib import *
DAY = 9
PART = 2

pInp = get_input(DAY)
ans = 0

class N:
    def __init__(self, s, g, id):
        self.s = [id for i in range(s)]
        self.gsize = g
        self.g = []

id = 0
nums = []
nodes = []

for i in pInp:
    nums += list(map(lambda x: int(x), list(i)))

while len(nums) > 1:
    new = N(nums.pop(0), nums.pop(0), id)
    nodes.append(new)
    id += 1

new = N(nums.pop(0), 0, id)
nodes.append(new)
id += 1

for i in range(len(nodes) - 1, 0, -1):
    l = len(nodes[i].s)
    moved = False
    for j in range(0, i):
        if (nodes[j].gsize - len(nodes[j].g) >= l):
            for k in range(l):
                nodes[j].g.append(i)
            moved = True
            newl = len(nodes[i].s)
            nodes[i].s = [0 for i in range(newl)]
            break
        if moved:
            break

for i in nodes:
    while len(i.g) < i.gsize:
        i.g.append(0)

id = 0
for i in nodes:

    for j in i.s:

        ans += j * id
        id += 1

    for j in i.g:

        ans += j * id
        id += 1
print()
submit(DAY, PART, ans)