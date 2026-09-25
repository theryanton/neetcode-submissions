class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = suffix[n-1] = 1

        for i in range(1, n, 1):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i, num in enumerate(nums):
            output[i] = prefix[i] * suffix[i]
        
        return output
