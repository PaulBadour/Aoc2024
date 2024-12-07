from aoclib import *
DAY = 7
PART = 1

pInp = get_input(DAY)
ans = 0

# Code

def test(target, nums):
    if len(nums) == 1:
        return target == nums[0]
    
    n1, n2 = nums.pop(0), nums.pop(0)

    return test(target, [n1 + n2] + nums) or test(target, [n1 * n2] + nums)

for i in pInp:
    nums = getints(i)

    target = nums.pop(0)

    if test(target, nums):
        ans += target

    

submit(DAY, PART, ans)