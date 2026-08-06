class Solution:
    def rob(self, nums: List[int]) -> int:
        s = len(nums)-1
        nums2 = {}

        def maximum(i, nums, ans):
            if (i <= s):
                if (i == 0):
                    ans[i] = 0
                elif (i == 1):
                    ans[i] = nums[0]
                else:
                    ans[i] = max(ans[i-1], ans[i-2] + nums[i-1])
                maximum(i+1, nums, ans)
            return ans
        
        ans = maximum(0, nums[:-1], {})

        for i in range(len(nums)-1):
            nums2[i] = nums[i+1]

        ans2 = maximum(0, nums2, {})
        
        if s > 0:
            return max(ans[s], ans2[s])
        else:
            return nums[0]