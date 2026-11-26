class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, combo, runningTotal):
            if i >= len(nums) or runningTotal > target:
                return
            
            if runningTotal == target:
                res.append(combo.copy())
                return
            
            combo.append(nums[i])
            dfs(i, combo, runningTotal + nums[i])
            combo.pop()
            dfs(i+1, combo, runningTotal)

        
        dfs(0, [], 0)
        return res


