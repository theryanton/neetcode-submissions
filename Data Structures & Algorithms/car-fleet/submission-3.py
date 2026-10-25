class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = []
        for p, s, in cars:
            time = float(target - p) / s
            fleets.append(time)

            while len(fleets) >= 2 and fleets[-2] >= fleets[-1]:
                fleets.pop()
        return len(fleets)