#题目
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""

"""
解题思路：
1.该题目应该将查找两个整数和转换为nums1 = target - nums2
2.对于python来说，可以通过字典同时记录数值与下标
3.在遍历数组时，可以记录下数值与下标到一个字典中，然后再遍历数组查找其互补数是否在字典中
通过空间复杂度换取时间复杂度，空间复杂度o(n)，时间复杂度o(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for ind,num in enumerate(nums):
            hasmap[num] = ind
        for i,num in enumerate(nums):
            j = hasmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
