class MyStack:

    def __init__(self):
        self.Q1=[]
        self.Q2=[]

    def push(self, x: int) -> None:
        while (len(self.Q1)!=0):
            self.Q2.append(self.Q1.pop(0))
        self.Q1.append(x)
        while (len(self.Q2)!=0):
            self.Q1.append(self.Q2.pop(0))

        #if not self.Q1:
        #    Q2=self.Q1.copy()
        #    self.Q1.clear()
        #    self.Q1.append(x)
        #    Q1=self.Q2.copy() 
        #else:
        #    self.Q1.append(x)

    def pop(self) -> int:
        if not self.Q1:
            return None
        return self.Q1.pop(0)

    def top(self) -> int:
        if not self.Q1:
            return None
        return self.Q1[0]

    def empty(self) -> bool:
         return len(self.Q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()