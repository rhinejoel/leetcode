class MinStack:
    def __init__(self):
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self._min)>0:
            if val < self._min[-1]: self._min.append(val)
            else: self._min.insert(-1, val)
        else: self._min.append(val)

    def pop(self) -> None:
        self._min.remove(self.stack[-1])
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min[-1]