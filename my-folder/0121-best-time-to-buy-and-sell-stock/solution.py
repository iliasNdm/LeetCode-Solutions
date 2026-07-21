class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for value in prices:
            new_profit = value - buy
            if new_profit < 0:
                buy = value
            elif new_profit > profit :
                profit = new_profit
            
        return profit 
                
                


