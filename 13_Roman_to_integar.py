class Solution:
    def romanToInt(self, s: str) -> int:
        has = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        previous = 0
        for i in reversed(s):
            current = has[i]
            if current < previous:
                total -= current
            else:
                total += current
            previous = current
        return total