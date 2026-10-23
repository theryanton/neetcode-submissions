class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        have = 0
        need = len(tmap)
        l = 0
        window = {} # current valid window

        reslen = float('inf')
        res = [-1, -1]

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1

                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]