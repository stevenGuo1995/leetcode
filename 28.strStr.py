class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        elif needle != 0 and needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello world!","hello"))