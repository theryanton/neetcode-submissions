class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniquestr = {} # letter -> index
        maxlength = 0
        l = 0

        for r in range(len(s)):
            if s[r] in uniquestr:
                l = max(uniquestr[s[r]] + 1, l)
            uniquestr[s[r]] = r
            maxlength = max(maxlength, r - l + 1)
        return maxlength