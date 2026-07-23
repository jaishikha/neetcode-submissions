class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]

            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, curr_profit)
            else:
                buy = sell

            sell += 1

        return max_profit