"""
67.二进制求和

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ab = '0b'+a
        bb = '0b'+b
        c = int(ab,2)+int(bb,2)
        return '{:b}'.format(c)


if __name__ == "__main__":
    s = Solution()
    c = s.addBinary('11','1')
    print(c)