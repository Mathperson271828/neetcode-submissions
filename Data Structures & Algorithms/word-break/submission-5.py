class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        for i in range(len(s)+1):
            if i == 0:
                dp[i] = True
            else:
                dp[i] = False
                for j in range(i):
                    if s[j:i] in wordDict and dp[j]:
                        dp[i] = True
                print(dp[i])
        
        return dp[len(s)]
                