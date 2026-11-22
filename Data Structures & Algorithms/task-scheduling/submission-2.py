class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        q = deque() # -cnt, cooldown
        time = 0
        while maxheap or q:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                task = 1 + heapq.heappop(maxheap)
                if task: # if anything not 0
                    q.append((task, time + n))
            if q and q[0][1] == time:
                readd = q.popleft()[0]
                heapq.heappush(maxheap, readd)
            
        return time
