class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cmap = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in cmap:
                stack.append(c)
            else:
                if stack == []: return False
                item = stack.pop()
                if cmap[c] != item: return False
        return True if stack == [] else False