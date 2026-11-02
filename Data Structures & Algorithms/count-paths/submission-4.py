class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        calculated = {}
        def numPaths(a, b):
            if (a == m-1 and b == n-1):
                return 1
            if (a >= m or b >= n) and (a, b) not in calculated:
                calculated[(a, b)] = 0
                return 0
            elif (a, b) not in calculated:
                calculated[(a, b)] = numPaths(a+1, b) + numPaths(a, b+1)
                return numPaths(a+1, b) + numPaths(a, b+1)
            else:
                return calculated[(a, b)]
        
        return numPaths(0, 0)