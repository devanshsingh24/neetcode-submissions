class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i.strip('-').isdigit():
                stack.append(int(i))
            elif i=='+':
                k=stack[-2]+stack[-1]
                stack.append(int(k))
            elif i=='C':
                stack.pop()
            elif i=='D':
                k=stack[-1]*2
                stack.append(int(k))
        return sum(stack)