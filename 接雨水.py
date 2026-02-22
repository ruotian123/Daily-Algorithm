#题目
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

"""
我的思路：
对于本题目而言，可以分别求解每个单位的雨水量，将它们加和，难点在于如何获取每个单位的雨水量
1.首先，每个单位的承接雨水量与两侧高度有关，所以可以通过两个指针分别表示两侧高度，一个从左向右移动，一个从右向左移动
2.当两个指针高度不等时，不妨可以认为该单位的雨水量是最小高度指针-该单位高度
时间复杂度o(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        ans = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += min(left_max, right_max) - height[left]
                left += 1
            else:
                ans += min(left_max, right_max) - height[right]
                right -= 1
        return ans
