class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = None
        max2 = None
        max3 = None

        for i in nums:
            if i==max1 or i==max2 or i==max3:
                continue
            if max1==None or i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif max2==None or i>max2:
                max3 = max2
                max2 = i
            elif max3==None or i > max3:
                max3=i

        return max1 if max3==None else max3