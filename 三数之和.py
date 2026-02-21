#三数之和
"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
"""

"""
我的思路：
1.首先返回的是数而非下标，可以对数组进行顺序排列，进而将s1+s2+s3=target转换成s1+s2=target-s3的问题
2.对于这样一个求两数之和的顺序数组，可以使用双向指针求解，target-s3进行外循环，s1+s2通过双向指针求
时间复杂度为o(n^2)
"""
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
