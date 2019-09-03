# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def evalRPN(self, tokens: list) -> int:
        ope=["+",'-','*','/']
        numstack=[]
        for i in tokens:
            if i in ope:
                b=numstack.pop(-1)
                a=numstack.pop(-1)
                if i=="+":
                    res=a+b
                if i=="-":
                    res=a-b
                if i=="*":
                    res=a*b
                if i=="/":
                    res=int(a/b)
                numstack.append(res)
            else:
                numstack.append(int(i))
        return numstack[-1]

print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

