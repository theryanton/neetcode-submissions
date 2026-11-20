class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for (x, y) in points:
            distance = (x - 0)**2 + (y - 0)**2
            heapq.heappush(distances, (-distance, (x, y)))
            if len(distances) > k:
                heapq.heappop(distances)

        res = []
        for distance, cords in distances:
            res.append(cords)
        return res
        

