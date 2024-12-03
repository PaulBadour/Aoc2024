from aoclib import *
import re
DAY = 3
PART = 2

pInp = get_input(DAY)
ans = 0

enabled = True

# Code
for i in pInp:
    m = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", i)
    for j in m:

        if j == 'do()':
            enabled = True
        elif j == "don't()":
            enabled = False
        elif enabled:
            i1 = int(j[4:j.index(',')])
            i2 = int(j[j.index(',') + 1:j.index(')')])
            ans += i1 * i2

submit(DAY, PART, ans)