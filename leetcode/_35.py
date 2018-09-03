class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums_len = len(nums)
        start = 0
        end = nums_len - 1
        if start == end:
            return start if target <= nums[start] else start+1
        while start < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start if target <= nums[start] else start+1



test = Solution()
print(test.searchInsert([1, 2, 3, 5, 7], 8))