class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        while index >= 0:
            if digits[index] < 9:
                digits[index] += 1
                break
            elif index == 0:
                return [1 if idx == 0 else 0 for idx in range(len(digits)+1)]
            else:
                digits[index] = 0
            index -= 1
        return digits

test = Solution()
print(test.plusOne([9, 9, 9]))
