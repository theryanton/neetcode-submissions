class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)

        def dfs(i, perm, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if pick[i] == False:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(i+1, perm, pick)
                    perm.pop()
                    pick[i] = False

        dfs(0, [], pick)
        return res