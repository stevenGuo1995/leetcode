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
    r = s.lengthOfLastWord('   ')
    print(r)