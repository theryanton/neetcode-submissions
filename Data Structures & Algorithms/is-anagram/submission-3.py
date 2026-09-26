class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = [0] * 26
        tmap = [0] * 26
        for c in range(len(s)):
            smap[ord(s[c]) - ord('a')] += 1
        for c in range(len(t)):
            tmap[ord(t[c]) - ord('a')] += 1
        return smap == tmap
