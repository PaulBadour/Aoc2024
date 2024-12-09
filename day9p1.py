from aoclib import *
DAY = 9
PART = 1

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

ind = 0
while len(nodes[-1].g) == 0:
    print(len(nodes))
    if len(nodes[ind].g) < nodes[ind].gsize:
        nodes[ind].g.append(nodes[-1].s.pop(-1))
        if len(nodes[-1].s) == 0:
            nodes.pop(-1)
            id -= 1
    else:
        ind += 1
        id -= 1

id = 0
for i in nodes:
    for j in i.s:
        ans += j * id
        id += 1

    for j in i.g:
        ans += j * id
        id += 1

submit(DAY, PART, ans)