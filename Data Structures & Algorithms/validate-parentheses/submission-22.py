class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack == []:
                    return False
                if c == ')':
                    element = stack.pop()
                    if element != '(':
                        return False
                elif c == '}':
                    element = stack.pop()
                    if element != '{':
                        return False
                elif c == ']':
                    element = stack.pop()
                    if element != '[':
                        return False
        return len(stack) == 0


