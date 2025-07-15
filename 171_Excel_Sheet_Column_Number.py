class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for j in columnTitle:
            total = total * 26 + (ord(j) - ord('A') + 1)
        return total