"""
题目

07.反转整数

给定一个 32 位有符号整数，将整数中的数字进行反转。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))
        r = int(s[::-1])
        if -2 ** 31 < r < 2 ** 31 - 1:
            if x >= 0:
                return r
            else:
                return -r
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    r = s.reverse(-12)
    print(r)
