class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookup = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in lookup: # open bracket
                stack.append(c)
            else:
                if stack == []: return False
                elif lookup[c] != stack.pop():
                    return False
        return len(stack) == 0