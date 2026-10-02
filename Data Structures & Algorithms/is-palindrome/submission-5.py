class Solution:
    def isPalindrome(self, s: str) -> bool:
        scrubbed = ""
        for c in s:
            if c.isalnum():
                scrubbed += c.lower()
        
        l = 0
        r = len(scrubbed) - 1
        while l < r:
            if scrubbed[l] != scrubbed[r]:
                return False
            l += 1
            r -= 1
            if l == r: l += 1
        return True