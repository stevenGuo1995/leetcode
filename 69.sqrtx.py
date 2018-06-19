"""
题目：67.x的平方根

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""

import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**0.5)


if __name__ == '__main__':
    s = Solution()
    r = s.mySqrt(5)
    print(r)
