class Solution(object):
    def sortedSquares(self, nums):
        nums1 = []
        for i in nums:
            nums1.append(i**2)
        return sorted(nums1)