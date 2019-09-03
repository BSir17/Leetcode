# -*- coding:utf-8 -*-
# Code by Fan.Bai

#可以用全排列来做
#传入左边有多少个括号，如果为待匹配为0，当前字符只能是左括号，否则可以是右括号或左括号
class Solution1:
    def generateParenthesis(self, n: int):
        self.res=[]
        self.n = n*2
        self.generate(0,0,"")
        return self.res
    def  generate(self,leftnum,wait,s):
        if len(s)==self.n-1:
            self.res.append(s+")")
            return
        if leftnum==self.n//2:
            self.generate(leftnum,wait,s+")")
        else:
            if wait==0:
                self.generate(leftnum+1,wait+1,s+"(")
            else:
                self.generate(leftnum + 1, wait + 1, s+"(")
                self.generate(leftnum , wait -1, s+")")

class Solution:
    def generateParenthesis(self, n: int):
        self.res=[]
        self.n = n
        self.generate(0,0,"")
        return self.res
    def  generate(self,l,r,s):
        if l<r or l>self.n or r>self.n:
            return
        if len(s)==2*self.n-1:
            self.res.append(s+')')
            return
        self.generate(l+1,r,s+'(')
        self.generate(l,r+1,s+')')


print(Solution().generateParenthesis(3))









