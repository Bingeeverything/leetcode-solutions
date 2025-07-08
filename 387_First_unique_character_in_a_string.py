from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx, val in enumerate(s):
            if count[val] == 1:
                return idx
                break
        else :
            return -1