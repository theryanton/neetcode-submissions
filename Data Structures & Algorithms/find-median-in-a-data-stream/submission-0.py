class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush_max(self.maxheap, num)
        
        if abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) > len(self.maxheap):
                element = heapq.heappop(self.minheap)
                heapq.heappush_max(self.maxheap, element)
            else:
                element = heapq.heappop_max(self.maxheap)
                heapq.heappush(self.minheap, element)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        else:
            return float((self.minheap[0] + self.maxheap[0]) / 2)
        
        