class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = 1

        profit = 0
        
        while a < b and b < len(prices):
            if (prices[a] >= prices[a+1] and b+1 < len(prices)):
                a += 1 
                b = a+1
            else:
                if (b < len(prices)-1):
                    if (prices[b] < prices[b+1]):
                        b += 1
                    else:
                        profit = max(profit, prices[b] - prices[a])
                        b += 1
                else:
                    profit = max(profit, prices[b] - prices[a])
                    a += 1
                    b = a+1

        return profit