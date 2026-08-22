class MyStack:

    def __init__(self):
        self.Q1=[]
        self.Q2=[]

    def push(self, x: int) -> None:
        self.Q2.append(x)
        # Step 2: move everything from Q1 to Q2
        while self.Q1:
            self.Q2.append(self.Q1.pop(0))
        # Step 3: swap Q1 and Q2
        self.Q1, self.Q2 = self.Q2, []
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