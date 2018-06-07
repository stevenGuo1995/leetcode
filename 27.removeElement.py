class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # while nums.count(val) > 0:
        #     del nums[nums.index(val)]
        # return len(nums)
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    r = s.removeElement([2,3,3,4],3)
    print(r)