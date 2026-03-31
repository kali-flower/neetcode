class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        go through entire input array 
        buy and sell pointers 
        track the max 
        if sell > buy --> update max 
        if buy > sell --> move left to right (current 
        price is no longer a good price to buy)
        ++ sell on every iteration 
        '''

        buy = 0
        sell = 1
        max_profit = 0 

        while sell < len(prices): 
            if prices[buy] < prices[sell]: 
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else: 
                buy = sell 
            sell += 1 

        return max_profit 
