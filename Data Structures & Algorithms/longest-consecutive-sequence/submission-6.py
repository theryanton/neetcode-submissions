class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 0

        for num in numset:
            if num - 1 in numset: continue
            count = 0
            while num + count in numset:
                count += 1
            res = max(count, res)

        return res