class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            s1 = nums[i]
            if s1 == nums[i - 1] and i > 0:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = s1 + nums[j] + nums[k]
                if s < 0:
                    j = j + 1
                elif s > 0:
                    k = k - 1
                else:
                    ans.append([s1,nums[j],nums[k]])
                    j = j + 1
                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
                    k = k - 1
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1
        return ans
