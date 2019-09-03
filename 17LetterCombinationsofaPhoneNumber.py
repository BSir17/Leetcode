# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def getcombine(self,s):
        if not s:
            return [[]]
        locnum=s[0]
        res=[]
        restres=self.getcombine(s[1:])
        for i in list(self.alist[int(locnum)]):
            for arest in restres:
                tmp=[i]+arest
                res.append(tmp)
        return res
    def letterCombinations(self, digits: str):
        if len(digits)<1:
            return []
        self.alist=[None,None,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res= self.getcombine(digits)
        res=["".join(i)for i in res]
        return res

print(Solution().letterCombinations('23'))











