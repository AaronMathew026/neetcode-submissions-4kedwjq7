class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index,price in enumerate(prices):
            for i in range(0,index):
                new_profit = price - prices[i]
                if new_profit > profit:
                    profit = new_profit

        return profit





        