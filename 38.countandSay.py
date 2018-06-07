class Solution(object):
    def countStr(self, s):
        count = 0
        ans = ''
        temp = s[0]

        return ans

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        while n > 1:
            ans = self.countStr(ans)
            n -= 1
            