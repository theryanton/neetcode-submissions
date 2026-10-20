class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1count = [0] * 26
        s2count = [0] * 26

        for r in range(len(s1)):
            s1count[ord(s1[r]) - ord('a')] += 1
            s2count[ord(s2[r]) - ord('a')] += 1
        
        if s1count == s2count: return True

        for r in range(len(s1), len(s2)):
            s2count[ord(s2[r]) - ord('a')] += 1
            s2count[ord(s2[r - len(s1)]) - ord('a')] -= 1

            if s1count == s2count: return True
        return False