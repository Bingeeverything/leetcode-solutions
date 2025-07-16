class Solution:
    def countAsterisks(self, s: str) -> int:
        total = 0
        inside = False

        for i in s:
            if i == '|':
                inside = not inside 
            elif i == '*' and not inside:
                total += 1

        return total
