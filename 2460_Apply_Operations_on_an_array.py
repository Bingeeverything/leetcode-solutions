class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *=  2
                nums[i + 1] = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        for j in range(left, len(nums)):
            nums[j] = 0
        return nums