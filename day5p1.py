from aoclib import *
DAY = 5
PART = 1

pInp = get_input(DAY)
ans = 0

class Node:
    nodes = []
    def __init__(self, n):
        self.value = n
        self.nexts = []
        Node.nodes.append(self)

    def selfValues(self):
        return [x.value for x in self.nexts]

    def addAfter(self, n):
        self.nexts.append(n)

    @staticmethod
    def findNode(n):
        for i in Node.nodes:
            if i.value == n:
                return i
        return None
    
    def dive(self, n):
        if n in self.selfValues():
            return True
        # for i in self.nexts:
        #     if i.dive(n):
        #         return True
            
        return False

for i in pInp[:pInp.index('')]:
    print(i)
    ns = getints(i)
    n = Node.findNode(ns[0])
    k = Node.findNode(ns[1])
    if n:
        if k:
            n.addAfter(k)
        else:
            n.addAfter(Node(ns[1]))
    else:
        l = Node(ns[0])
        if k:
            l.addAfter(k)
        else:
            l.addAfter(Node(ns[1]))


for i in pInp[pInp.index('') + 1:]:
    ns = getints(i)
    print(ns)
    good = True
    for j in range(len(ns) - 1):
        if not Node.findNode(ns[j]).dive(ns[j + 1]):
            good = False
            break

    if good:
        print(len(ns) / 2)
        ans += ns[int(len(ns) / 2)]



submit(DAY, PART, ans)