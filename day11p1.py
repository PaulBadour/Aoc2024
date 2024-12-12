from aoclib import *
DAY = 11
PART = 1

pInp = get_input(DAY)
ans = 0
start = None
last = None

class Node:
    def __init__(self, num):
        self.n = num
        self.next = None
        self.prev = None

    def change(self):
        if self.n == 0:
            self.n = 1

        elif len(str(self.n)) % 2 == 0:
            new = Node(int(str(self.n)[int(len(str(self.n))/2):]))
            self.n = int(str(self.n)[:int(len(str(self.n))/2)])
            new.next = self.next
            if self.next:
                self.next.prev = new
            self.next = new

        else:
            self.n *= 2024

    def getNodes(self):
        if self.next == None:
            return [self]
        return [self] + self.next.getNodes()

for i in getints(pInp[0]):
    n = Node(i)
    if start == None:
        start = n
    if last != None:
        n.prev = last
        last.next = n

    last = n
ns = set()
for i in range(25):
    ns = set()
    cn = start
    while cn.next != None:
        ns.add(cn)
        cn = cn.next
    ns.add(cn)
    for i in ns:
        i.change()


ns = set()
cn = start
while cn.next != None:
    ns.add(cn)
    cn = cn.next
ns.add(cn)

ans = len(ns)
submit(DAY, PART, ans)