class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(tokens[i]))
        return stack[0]