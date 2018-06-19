"""
题目

53.最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 法一 穷举 （超时）
        # maxSum = float("-inf")
        # l = len(nums)
        # for i in range(l):
        #     sum = 0
        #     for j in range(i, l):
        #         sum += nums[j]
        #         if sum > maxSum:
        #             maxSum = sum
        #
        # return maxSum

        # 法二
        max = float("-inf")
        sum = 0
        for i in nums:
            sum += i
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max


if __name__ == "__main__":
    s = Solution()
    m = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # m = s.maxSubArray([-2,-1])
    print(m)
