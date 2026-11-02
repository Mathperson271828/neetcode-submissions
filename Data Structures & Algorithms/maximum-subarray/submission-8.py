class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = tot = nums[0]
        for i in range(len(nums)-1):
            tot = max(tot+nums[i+1], nums[i+1])
            ans = max(ans, tot)
            
        return ans