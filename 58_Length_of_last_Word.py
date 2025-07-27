class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spl = s.split()
        return len(spl[-1])