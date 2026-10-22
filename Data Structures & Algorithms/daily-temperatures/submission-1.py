class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                pastDay, pastTemp = stack.pop()
                res[pastDay] = i - pastDay
            stack.append((i, temp))
        return res