class Solution:

    # My solution:
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp = nums[lastNonZero]
                nums[lastNonZero]=nums[i]
                nums[i] = tmp
                lastNonZero += 1


    # Optimal Solution:
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] == 0:
                while fast < len(nums) - 1 and nums[fast] == 0:
                    fast += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1