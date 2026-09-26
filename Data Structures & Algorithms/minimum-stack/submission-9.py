class MinStack:
    from collections import deque
    import math

    debug = False

    def __init__(self):
        self.stack = deque()
        self.min_val = math.inf
        

    def push(self, val: int) -> None:
        self.min_val = min(val, self.min_val) if self.stack else val
        self.stack.appendleft((val, self.min_val)) 
        if self.debug: print(self.stack)

    def pop(self) -> None:
        self.stack.popleft()
        if self.stack: self.min_val = self.stack[0][1]
        if self.debug: print(self.stack)

    def top(self) -> int:
        return self.stack[0][0]
        

    def getMin(self) -> int:
        return self.stack[0][1]
        