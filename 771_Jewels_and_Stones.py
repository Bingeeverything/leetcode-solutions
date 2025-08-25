class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        has = {}
        count = 0
        for i in jewels:
            has[i] = "."
        for i in stones:
            if i in has:
                count += 1
        return count