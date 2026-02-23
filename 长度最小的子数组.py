class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = len(nums) + 1
        left = 0
        s = 0
        for right,x in enumerate(nums):
            s += x
            while (s - nums[left]) >= target:
                s -= nums[left]
                
                left +=1
            if s >= target:
                ans = min(ans,right-left+1)
        if ans < n + 1:
            return ans
        else:
            return 0
