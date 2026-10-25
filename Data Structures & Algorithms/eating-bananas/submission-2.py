class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # perform binary search but instead of looking for
        # a target, we'll be calculating the min eating speed
        l = 1
        r = max(piles) # max eating speed has to be max piles

        minspeed = r

        while l <= r:
            k = l + (r-l) // 2
            # for this k, we'll calculate how many hrs needed to finish all piles
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            # has to be ceil as we round partial hours up to fullest integer

            if hours <= h:
                minspeed = min(minspeed, k)
                r = k - 1
            else:
                l = k + 1
        return minspeed
            
            