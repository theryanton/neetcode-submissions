class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currentList, runningTotal):
            if runningTotal == target:
                res.append(currentList.copy())
                return
            if i >= len(nums) or runningTotal > target:
                return
            currentList.append(nums[i])
            dfs(i, currentList, runningTotal + nums[i])
            currentList.pop()
            dfs(i+1, currentList, runningTotal)

        dfs(0, [], 0)
        return res