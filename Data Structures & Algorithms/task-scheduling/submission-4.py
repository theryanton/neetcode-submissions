class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [cnt for cnt in count.values()]
        heapq.heapify_max(max_heap)

        cycles = 0
        q = deque()
        while q or max_heap:
            cycles += 1
            if max_heap:
                task = heapq.heappop_max(max_heap)
                task -= 1
                if task > 0:
                    q.append((task, cycles + n))
            else:
                if q:
                    cycles = q[0][1]
            if q and q[0][1] == cycles:
                task = q.popleft()[0]
                heapq.heappush_max(max_heap, task)
        return cycles
