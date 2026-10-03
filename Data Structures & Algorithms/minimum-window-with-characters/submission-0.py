class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        tcount = {}
        for c in t:
            if c not in tcount:
                tcount[c] = 1
            else: tcount[c] += 1

        l = 0
        have, need = 0, len(tcount)
        res_len = float("inf")
        res_bounds = [-1, -1]
        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in tcount and window[s[r]] == tcount[s[r]]:
                have += 1
            
            while have == need: #still looking for shortest window
                if r-l+1 < res_len:
                    res_len = r-l+1
                    res_bounds = [l, r]
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
        l, r = res_bounds
        return s[l : r + 1] if res_len != float("inf") else ""




