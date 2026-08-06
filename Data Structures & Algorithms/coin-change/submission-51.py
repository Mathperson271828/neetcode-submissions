class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = {}
        ans[0] = 0

        for i in range(1, amount+1):
            x = sys.maxsize
            for val in coins:
                if i-val >= 0 and ans[i-val] != -1:
                    x = min(x, ans[i-val]+1)
        
            if x == sys.maxsize:
                ans[i] = -1
            else:
                ans[i] = x

        return ans[amount]
