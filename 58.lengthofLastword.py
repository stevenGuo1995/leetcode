"""
题目：

58. 最后一个单词的长度

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = s.split()
        if len(r) == 0:
            return 0
        return len(r[-1])


if __name__ == "__main__":
    s = Solution()
    r = s.lengthOfLastWord('hello world nihao')
    print(r)
