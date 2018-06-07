class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 2, 3, 4, 5], 2))
