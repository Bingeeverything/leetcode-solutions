class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty_bottles = 0
        while numBottles > 0:
            count += numBottles
            numBottles += empty_bottles
            empty_bottles = numBottles % numExchange
            numBottles = (numBottles // numExchange)

        return count