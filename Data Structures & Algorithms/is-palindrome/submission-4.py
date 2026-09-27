class Solution:
    def isPalindrome(self, s: str) -> bool:
        scrubbed = ''
        for c in s:
            if c.isalnum():
                scrubbed += c.lower()
            
        i = 0
        j = len(scrubbed) - 1
        while i < j:
            if scrubbed[i] == scrubbed[j]:
                i += 1
                j -= 1
            else: return False
        return True
            