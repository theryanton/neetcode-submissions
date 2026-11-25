class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush_max(maxheap, (distance, [x, y]))
            if len(maxheap) > k:
                heapq.heappop_max(maxheap)
        
        res = []
        for distance, coords in maxheap:
            res.append(coords)
        return res