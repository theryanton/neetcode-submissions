class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        maxlen = 0
        for c in chars:
            length = 0
            l = 0
            freq = 0
            for r in range(len(s)):
                if s[r] == c:
                    freq += 1
                while (r - l + 1) - freq > k:
                    if s[l] == c: freq -= 1
                    l += 1
                length = max(length, r-l+1)
            maxlen = max(length, maxlen)
        return maxlen

