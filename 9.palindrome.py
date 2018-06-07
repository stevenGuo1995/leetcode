class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s1 = str(x)
        s2 = s1[::-1]
        return s1 == s2


if __name__ == "__main__":
    s= Solution()
    r = s.isPalindrome(669)
    print(r)
