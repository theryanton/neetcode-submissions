class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ccount = {}

        l = maxfrequency = length = 0
        for r in range(len(s)):
            ccount[s[r]] = ccount.get(s[r], 0) + 1
            maxfrequency = max(ccount[s[r]], maxfrequency) # which letter is more common
            while r - l - maxfrequency >= k:
                ccount[s[l]] -= 1
                l += 1
            length = max(r - l + 1, length)
        return length

