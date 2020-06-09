class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        mini = prices[0]
        maxi = prices[-1]
        profitL = [0]*len(prices)
        profitR = [0]*(len(prices)+1)
        
        for i in range(0,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            profitL[i] = max(profitL[i-1],(prices[i]-mini))
        
        for i in range(len(prices)-1, -1, -1):
            if prices[i]>maxi:
                maxi = prices[i]
            profitR[i] = max((maxi-prices[i]),profitR[i+1])
            
        maxProfit = 0
        for i in range(0,len(prices)):
            maxProfit = max(maxProfit,(profitL[i]+profitR[i]))
        return maxProfit  
