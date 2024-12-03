from aoclib import *
import re
DAY = 3
PART = 1

pInp = get_input(DAY)
ans = 0

# Code
for i in pInp:
    m = re.findall("mul\(\d+,\d+\)", i)
    for j in m:
        i1 = int(j[4:j.index(',')])
        i2 = int(j[j.index(',') + 1:j.index(')')])
        ans += i1 * i2

submit(DAY, PART, ans)