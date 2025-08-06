class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        has = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in has:
                count += has[nums[i]]

            has[nums[i]] = has.get(nums[i] , 0) + 1
        return count