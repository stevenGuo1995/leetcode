class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            print(i,num)
            if target - num in d:
                return [d[target - num], i]
            d[num] = i


if __name__ == "__main__":
    n = [2, 7, 11, 15]
    t = 9
    s = Solution()
    print(s.twoSum(n, t))
