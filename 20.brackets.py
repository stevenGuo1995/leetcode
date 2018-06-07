class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i, c in enumerate(s):
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")" and len(stack) > 0:
                t = stack.pop()
                if t != '(':
                    return False
            elif c == "]" and len(stack) > 0:
                t = stack.pop()
                if t != '[':
                    return False
            elif c == "}" and len(stack) > 0:
                t = stack.pop()
                if t != '{':
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    r = s.isValid('(){}[]')
    print(r)
