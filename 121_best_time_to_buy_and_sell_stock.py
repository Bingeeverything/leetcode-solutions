class Solution(object):
    def maxProfit(self, prices):
        min_prices = float('inf')
        max_profit = -float('inf')
        for i in prices:
            if i < min_prices:
                min_prices = i
            if i - min_prices > max_profit:
                max_profit = i - min_prices
        return max_profit