class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        yo = set(nums)
        longest = 0
        for i in yo:
            if i - 1 not in yo:
                current = i
                streak =  1
                
                while current +1 in yo:
                    current += 1
                    streak  += 1
                longest = max(longest, streak)
        return longest