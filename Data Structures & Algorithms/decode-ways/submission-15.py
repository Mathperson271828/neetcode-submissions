class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        ans = {}

        def dfs(i):
            if i not in ans:
                if (i >= n):
                    ans[i] = 1
                else:
                    if s[i] == '0' and (i == 0 or i != n-1):
                        ans[i] = 0
                    elif ((s[i] == '1' and i+1 < n and s[i+1] != '0') or (s[i] == '2' 
                            and i+1 < n and int(s[i+1]) <= 6 and s[i+1] !=
                            '0')):
                        ans[i] = dfs(i+1) + dfs(i+2)
                    elif ((s[i] == '1' and i+1 < n and s[i+1] == '0') or (s[i] == '2' 
                            and i+1 < n and s[i+1] == '0')):
                        ans[i] = dfs(i+2)
                    else:
                        ans[i] = dfs(i+1)
            return ans[i]
        
        return dfs(0)