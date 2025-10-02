class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty_bottles = numBottles
        count += numBottles
        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            numBottles = 1
            count += 1
            empty_bottles += 1
            numExchange += 1
                
        return count