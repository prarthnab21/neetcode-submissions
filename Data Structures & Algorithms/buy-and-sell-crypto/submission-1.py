class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            if minprice > prices[i]:
                minprice = prices[i]

            if profit < (prices[i] - minprice):
                profit = prices[i] - minprice
        
        return profit
        #time = O(n) n: prices
        #space = O(n)