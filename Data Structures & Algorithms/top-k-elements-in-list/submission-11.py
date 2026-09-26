class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        sorteddict = sorted(count, key=count.get, reverse=True)
        res = []
        for i in range(k):
            res.append(sorteddict[i])
        return res