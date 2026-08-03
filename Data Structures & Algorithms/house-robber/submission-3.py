class Solution:
    def rob(self, nums: List[int]) -> int:
        s = len(nums)
        ans = {}

        def maximum(i):
            if (i <= s):
                if (i == 0):
                    ans[i] = 0
                elif (i == 1):
                    ans[i] = nums[0]
                else:
                    ans[i] = max(ans[i-1], ans[i-2] + nums[i-1])
                maximum(i+1)
        
        maximum(0)
        
        return ans[s]