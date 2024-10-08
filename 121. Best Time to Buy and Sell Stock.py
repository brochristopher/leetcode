class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price_so_far = -1
        best_profit = 0

        for i in range(len(prices)):
            if lowest_price_so_far == -1:
                lowest_price_so_far = prices[i]
            elif prices[i] < lowest_price_so_far:
                lowest_price_so_far = prices[i]
            if prices[i] - lowest_price_so_far > best_profit:
                best_profit = prices[i] - lowest_price_so_far

        return(best_profit)
