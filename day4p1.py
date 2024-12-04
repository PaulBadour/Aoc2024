from aoclib import *
import re
DAY = 4
PART = 1

pInp = get_input(DAY)
ans = 0

for i in pInp:
    ans += len(re.findall('XMAS', i))
    ans += len(re.findall('SAMX', i))


for i in range(len(pInp) - 3):
    for j in range(len(pInp[0])):
        if f"{pInp[i][j]}{pInp[i+1][j]}{pInp[i+2][j]}{pInp[i+3][j]}" in ('XMAS', "SAMX"):
            ans += 1

for i in range(len(pInp) - 3):
    for j in range(len(pInp[0]) - 3):
        if f"{pInp[i][j]}{pInp[i+1][j+1]}{pInp[i+2][j+2]}{pInp[i+3][j+3]}" in ('XMAS', "SAMX"):
            ans += 1

for i in range(3, len(pInp)):
    for j in range(len(pInp[0]) - 3):
        if f"{pInp[i][j]}{pInp[i-1][j+1]}{pInp[i-2][j+2]}{pInp[i-3][j+3]}" in ('XMAS', "SAMX"):
            ans += 1


submit(DAY, PART, ans)