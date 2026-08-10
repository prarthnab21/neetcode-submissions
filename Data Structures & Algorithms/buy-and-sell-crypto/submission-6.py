class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]

            if profit < prices[i] - minPrice:
                profit = prices[i] - minPrice

        return profit