class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        has = {}
        for i, val in enumerate(nums):
            if val in has:
                if i - has[val] <= k:
                    return True
            has[val] = i
        return False
