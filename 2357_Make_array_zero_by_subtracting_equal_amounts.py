class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        s.discard(0)
        if not s:
            return 0
        else:
            return len(s)