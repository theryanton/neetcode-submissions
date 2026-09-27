class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        char_map = {')': '(', ']': '[', '}': '{'}
    
        for c in s:
            if c in char_map: # close
                if stack != [] and stack[-1] == char_map[c]: #make sure its not all closing bracket
                    stack.pop()
                else: return False
            else: stack.append(c) # open bracket

        return len(stack) == 0



            