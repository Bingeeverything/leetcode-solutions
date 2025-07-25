class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        has = {}
        maxlen = 0
        start = 0

        for i, val in enumerate(s):
            if val in has and has[val] >= start:
                start = has[val] + 1  # Move the start to one after the last occurrence
            has[val] = i
            maxlen = max(maxlen, i - start + 1)

        return maxlen
