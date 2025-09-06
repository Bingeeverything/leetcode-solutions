class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[j] = 0
                j += 1
        while j < len(nums):
            nums[j] = 1
            j += 1
        return nums