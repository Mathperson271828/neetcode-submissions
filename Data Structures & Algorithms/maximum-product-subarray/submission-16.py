class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        l = {}
        s = {}
        
        for i in range(n):
            if (i == 0):
                l[i] = nums[0]
                s[i] = nums[0]
            else:
                if (nums[i] > 0):
                    l[i] = max(nums[i], l[i-1] * nums[i])
                    s[i] = min(nums[i], s[i-1] * nums[i])
                elif (nums[i] < 0):
                    l[i] = max(nums[i], s[i-1] * nums[i])
                    s[i] = min(nums[i], l[i-1] * nums[i])
                else:
                    l[i] = 0 
                    s[i] = 0
        
        return max(l.values())