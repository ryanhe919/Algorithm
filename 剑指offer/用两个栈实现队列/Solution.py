class CQueue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value):
        self.stack_1.append(value)

    def deleteHead(self):
        if self.stack_2:
            return self.stack_2.pop()
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            if self.stack_2:
                return self.stack_2.pop()
            else:
                return -1