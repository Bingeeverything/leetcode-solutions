class MyQueue:

    def __init__(self):
        self.yo1 = []
        self.yo2 = []

    def push(self, x: int) -> None:
        self.yo1.append(x)

    def pop(self) -> int:
        if not self.yo2:
            while self.yo1:
                self.yo2.append(self.yo1.pop())
        if self.yo2:
            return self.yo2.pop()
        return -1


    def peek(self) -> int:
        if not self.yo2:
            while self.yo1:
                self.yo2.append(self.yo1.pop())
        if self.yo2:
            return self.yo2[-1]
        return -1


    def empty(self) -> bool:
        if len(self.yo1) == 0 and len(self.yo2) == 0:
            return True
        else:
            return False

