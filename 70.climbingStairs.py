"""
题目：70.爬楼梯

假设你正在爬楼梯。需要 n 步你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            nums = [1, 2]
            i = 2
            while n > 2:
                a = nums[-1] + nums[-2]
                nums.append(a)
                n-=1
            return a


if __name__ == "__main__":
    s = Solution()
    c = s.climbStairs(35)
    print(c)
