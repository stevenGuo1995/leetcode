"""
题目

66. 加一


给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = ''
        for i in digits:
            res += str(i)
        t = int(res) +1
        ans = []
        for x in str(t):
            ans.append(int(x))
        return ans


if __name__ == "__main__":
    s = Solution()
    r = s.plusOne([1,2,3])
    print(r)