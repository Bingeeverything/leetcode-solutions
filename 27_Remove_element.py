class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
            
        for j in range(left, len(nums)):
            nums[j] = 0
        return left