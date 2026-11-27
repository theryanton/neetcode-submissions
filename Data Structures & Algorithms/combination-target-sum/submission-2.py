class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, combo, runningTotal):            
            if runningTotal == target:
                res.append(combo.copy())
                return
            
            for j in range(i, len(nums)):
                if runningTotal + nums[j] > target:
                    return
                combo.append(nums[j])
                dfs(j, combo, runningTotal + nums[j])
                combo.pop()

        
        dfs(0, [], 0)
        return res


