class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(index: int, remaining: int, path: List[int]) -> None:
            if remaining > 0:
                dfs(index, remaining - nums[index], path + [nums[index]])
                if (index+1 < len(nums)):
                    dfs(index+1, remaining, path)
            elif remaining == 0:
                ans.append(path)
            
        dfs(0, target, [])
    
        return ans
        
        
        
        