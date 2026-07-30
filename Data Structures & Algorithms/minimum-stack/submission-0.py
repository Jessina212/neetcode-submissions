class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self) -> int:

        if len(self.stack) != 0:
            t = self.stack.pop()
            self.stack.append(t)
            return t

    def getMin(self) -> int:
        if len(self.stack) != 0:
            return sorted(self.stack)[0]
        
