class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for ind,num in enumerate(nums):
            hasmap[num] = ind
        for i,num in enumerate(nums):
            j = hasmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
