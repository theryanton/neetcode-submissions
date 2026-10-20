class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        maxfreq = 0
        length = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxfreq = max(maxfreq, window[s[r]])

            while (r-l+1) - maxfreq > k:
                window[s[l]] -= 1
                l += 1
            length = max(length, r-l+1)
        return length