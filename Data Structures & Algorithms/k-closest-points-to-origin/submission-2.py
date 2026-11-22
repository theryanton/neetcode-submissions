class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxheap = []
        for x, y in points:
            distance = (x - 0)**2 + (y - 0)**2
            heapq.heappush(maxheap, (-distance, (x, y)))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        res = []
        for distance, coord in maxheap:
            res.append(coord)
        return res