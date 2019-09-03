# -*- coding:utf-8 -*-
# Code by Fan.Bai

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack=[]
        self.datastack=[]

    def push(self, x: int) -> None:
        self.datastack.append(x)
        if x<=self.getMin():
            self.minstack.append(x)
    def pop(self) -> None:
        temp=self.datastack[-1]
        self.datastack.pop(-1)
        if temp==self.getMin():
            self.minstack.pop(-1)
    def top(self) -> int:
        return self.datastack[-1]
    def getMin(self) -> int:
        if len(self.minstack)>0:
            return self.minstack[-1]
        else:
            return float('inf')

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())









