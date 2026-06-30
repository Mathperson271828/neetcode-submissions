class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, num in enumerate(nums):
            target = -num

            a = i + 1
            b = len(nums) - 1

            while a < b:
                if (nums[a] + nums[b] == target):
                    ans.add((num, nums[a], nums[b]))
                    a = a + 1
                    b = b - 1
                elif (nums[a] + nums[b] < target):
                    a = a + 1
                else:
                    b = b - 1
            
        key = [list(t) for t in ans]

        return key