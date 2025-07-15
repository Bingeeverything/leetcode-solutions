class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[-1]
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
                char = shortest[i]
                for word in strs:
                    if not word:
                        return ""
                    if word[i] != char:
                        return shortest[:i]
        return shortest