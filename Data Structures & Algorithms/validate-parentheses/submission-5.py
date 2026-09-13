class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            # can only add open brackets OR last
            if ch in '({[':
                stack.append(ch)
            elif stack:
                if stack[-1] == '(' and ch == ')':
                    stack.pop()
                elif stack[-1] == '[' and ch == ']':
                    stack.pop()
                elif stack[-1] == '{' and ch == '}':
                    stack.pop()
                else:
                    return False
            else: 
                return False
        # print(stack)
        return stack == []