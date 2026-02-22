#题目
"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
"""

"""
我的思路：
对于本问题来说，可以使用双指针移动来求解，不妨设左右两侧各有一个木板，这时可以求得一个容积，然后移动木板向里面
移动过程中，只有木板变高才可能导致容积可能变大，因此，移动时只需要比较两边木板长度，移动矮一侧木板即可
时间复杂度o(n)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        result = 0
        while left < right:
            ans = min(height[left],height[right]) * (right - left)
            result = max(result, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
