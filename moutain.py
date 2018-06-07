class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 3:
            return 0
        else:
            B = []
            for i in range(1, len(A) - 1):
                if A[i - 1] < A[i] > A[i + 1]:
                    B.append(i)
            if len(B) > 0:
                C = []
                for i in range(len(B)):
                    C.append([])
                    t = B.pop()+1
                    C[i].append(t-1)
                    while A[t-1] > A[t]:
                        C[i].append(A[t])
                        t+=1
                print(C)
            else:
                return 0


if __name__ == '__main__':
    s = Solution()
    r = s.longestMountain([1, 2, 3, 2, 1, 2, 1])
    # print(r)