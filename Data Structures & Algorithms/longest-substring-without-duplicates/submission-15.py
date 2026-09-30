class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniquestr = set()
        maxlength = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in uniquestr:
                uniquestr.remove(s[l])
                l+=1
            uniquestr.add(s[r])
            maxlength = max(maxlength, r - l + 1)
        return maxlength