class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

        # for x in nums:
        #     while nums.count(x) > 1:
        #         del nums[nums.index(x)]
        # return len(nums)

        # news_ids = []
        # for id in nums:
        #     if id not in news_ids:
        #         news_ids.append(id)
        # return len(news_ids)

        # if len(nums) < 2:
        #     return len(nums)
        # else:
        #     j = 0
        #     i = 1
        #     while i < len(nums):
        #         if nums[j] == nums[i]:
        #             i += 1
        #         else:
        #             j += 1
        #             nums[j] = nums[i]
        #             i += 1
        #     return j + 1


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    i = s.removeDuplicates(nums)
    # for x in range(i):
    print(nums)
