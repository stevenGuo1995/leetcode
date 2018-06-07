class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = len(s)
        r = 0
        for i in range(l):
            if i > 0 and d[s[i - 1]] < d[s[i]]:
                r = r + d[s[i]] - 2 * d[s[i - 1]]
            else:
                r += d[s[i]]
        return r


if __name__ == "__main__":
    s = Solution()
    r = s.romanToInt('MCM')
    print(r)
