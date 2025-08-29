class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        count = 1
        
        while i > 0:
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    nums.pop(i)
            else:
                count = 1
            i -= 1
            
        return len(nums)