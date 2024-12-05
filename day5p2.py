from aoclib import *
DAY = 5
PART = 2

pInp = get_input(DAY)
ans = 0

print(pInp)

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
    #print(i)
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
    print(i)
    ns = getints(i)
    good = True
    for j in range(len(ns) - 1):
        if not Node.findNode(ns[j]).dive(ns[j + 1]):
            print(f"Found Bad: {ns}")
            bads = list(map(lambda x: Node.findNode(x), ns))
            while True:
                swapped = False

                i = 0

                while i < len(bads) - 1:
                    if not bads[i].dive(bads[i + 1].value):
                        temp = bads[i]
                        bads[i] = bads[i + 1]
                        bads[i + 1] = temp
                        swapped = True
                        #input(f"swapped {i}")

                    i += 1

                if not swapped:
                    break

            ans += bads[int(len(bads) / 2)].value
            break


        



submit(DAY, PART, ans)