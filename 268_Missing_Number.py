class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        has = {}
        for num in nums:
            has[num] = True
        for i in range(len(nums) + 1):
            if i not in has:
                return i
        return -1