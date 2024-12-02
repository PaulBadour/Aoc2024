from aoclib import *
import re
DAY = 2
PART = 1

pInp = get_input(DAY)
ans = 0

for i in pInp:
    nums = re.findall("\d+", i)
    nums = [int(j) for j in nums]
    good = True
    decr = 1

    for j in range(len(nums) - 1):
        if j == 0:
            if nums[j + 1] < nums[j]:
                decr = -1
        
        if not (nums[j + 1] == nums[j] + decr or nums[j + 1] == nums[j] + (2 * decr) or nums[j + 1] == nums[j] + (3 * decr)):
            good = False
            break

    if good:
        ans += 1

submit(DAY, PART, ans)