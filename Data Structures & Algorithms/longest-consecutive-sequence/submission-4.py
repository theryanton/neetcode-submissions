class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortnums = set(nums)
        maxim = 0
        for num in sortnums:
            if num - 1 not in sortnums:
                length = 1
                while num + length in sortnums:
                    length += 1
                maxim = max(maxim, length)
        return maxim