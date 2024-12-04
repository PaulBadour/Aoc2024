from aoclib import *
import re, copy
DAY = 2
PART = 2

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
            

    if good == True:
        ans += 1
        continue

    for k in range(len(nums)):
        newn = copy.deepcopy(nums)
        del newn[k]
        decr = 1
        good = True
        for j in range(len(newn) - 1):
            if j == 0:
                if newn[j + 1] < newn[j]:
                    decr = -1
            
            if not (newn[j + 1] == newn[j] + decr or newn[j + 1] == newn[j] + (2 * decr) or newn[j + 1] == newn[j] + (3 * decr)):
                good = False

        if good:
            ans += 1
            break
        

submit(DAY, PART, ans)