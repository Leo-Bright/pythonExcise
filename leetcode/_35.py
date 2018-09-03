class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx in range(len(nums)):
            if nums[idx] >= target:
                return idx
            elif idx == len(nums)-1:
                return len(nums)
            else:
                continue


test = Solution()
print(test.searchInsert([1, 2, 3, 5, 7], 8))