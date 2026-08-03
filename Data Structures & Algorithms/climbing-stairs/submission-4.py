class Solution:
    def climbStairs(self, n: int) -> int:
        val = {}
        def calc(i, n):
            if i <= n:
                if (i == 0):
                    val[i] = 1
                elif (i == 1):
                    val[i] = 1
                else:
                    val[i] = val[i-1] + val[i-2]
                calc(i+1, n)

        calc(0, n)
        return val[n]
                

