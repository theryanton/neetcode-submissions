class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()] # frq of tasks
        heapq.heapify(maxheap)

        cycles = 0
        q = deque() # -cnt, cooldown
        while q or maxheap:
            cycles += 1

            if maxheap:
                task = heapq.heappop(maxheap)
                task += 1
                if task < 0:
                    q.append((task, cycles + n))        
            else:
                if q:
                    cycles = q[0][1]
            if q and q[0][1] == cycles:
                    heapq.heappush(maxheap, q.popleft()[0])
        return cycles

