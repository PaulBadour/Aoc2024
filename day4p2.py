from aoclib import *
import re
DAY = 4
PART = 2
pInp = get_input(DAY)
ans = 0




for i in range(1, len(pInp) - 1):
    for j in range(1, len(pInp[0])-1):
        if pInp[i][j] == 'A' and (pInp[i-1][j-1], pInp[i+1][j+1]) in (('M', 'S'), ('S', 'M')) and (pInp[i+1][j-1], pInp[i-1][j+1]) in (('M', 'S'), ('S', 'M')):
            ans += 1



submit(DAY, PART, ans)