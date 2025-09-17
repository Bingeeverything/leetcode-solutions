class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in has:
                return idx, has[diff]
            has[val] = idx
