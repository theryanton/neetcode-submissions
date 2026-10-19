class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: # num -> freq
            count[num] = count.get(num, 0) + 1

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            while len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for item in heap:
            res.append(item[1])
        return res