from itertools import combinations
from collections import OrderedDict


test=[i for i in range(len(A))]



test=[i for i in range(len(A))]
nums ={}
for i in range(len(A)):
    nums[i] = A[i]
nums =OrderedDict(sorted(nums.items(), key=lambda t: t[1],reverse=True))




ans=0

for comb in combinations(nums,3):
    if nums[comb[0]] + nums[comb[1]] > nums[comb[2]] and nums[comb[2]] + nums[comb[1]] > nums[comb[0]] and nums[comb[0]] + nums[comb[2]] > nums[comb[1]]:
        ans = (nums[comb[0]] +nums[comb[1]] + nums[comb[2]])
        break


if ans == 0:
    print(-1)
else:
    print(ans)




