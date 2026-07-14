class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        a = 0
        b = len(nums)-1
        res = nums[0]

        while (a <= b):
            if nums[a] < nums[b]:
                if nums[a] < res:
                    res = nums[a]
                    index = a
                break
            
            m = (a+b)//2
            if nums[m] < res:
                res = nums[m]
                index = m

            if nums[m] >= nums[a]:
                a = m+1
            else:
                b = m-1
        
        a = 0
        b = len(nums)-1
        ans = -1

        while (a <= b):
            m = (a+b)//2

            if nums[(m + index) % len(nums)] == target:
                ans = (m + index) % len(nums)
                break

            if nums[(m + index) % len(nums)] < target:
                a = m+1
            elif nums[(m + index) % len(nums)] > target:
                b = m-1

        return ans
            
        
