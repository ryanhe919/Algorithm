** 方法1：** 栈
push：把元素push入栈1

pop: 如果栈2有元素直接从栈2pop出，如果没有将栈1元素全部pop出并push到栈2 然后从栈2 pop出。
``` python
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
```