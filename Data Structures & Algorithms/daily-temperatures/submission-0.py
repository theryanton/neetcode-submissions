class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackDay = stack.pop()
                res[stackDay] = day - stackDay
            stack.append((temp, day))
        return res

            