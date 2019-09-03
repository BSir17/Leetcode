# -*- coding:utf-8 -*-
# Code by Fan.Bai

import numpy as np

#用递归
class Solution1(object):
    def sublcs(self, a, b):
        if len(a) == 0 or len(b) == 0:
            self.res[len(a) - 1][len(b) - 1] = 0
            return 0
        if a[-1] == b[-1]:
            ress = self.sublcs(a[:-1], b[:-1]) + 1
            self.res[len(a) - 1][len(b) - 1] = ress
            return ress
        else:
            ress = max([self.sublcs(a[:-1], b), self.sublcs(a, b[:-1])])
            self.res[len(a) - 1][len(b) - 1] = ress
            return ress

    def lcs(self, a, b):
        ax = len(a)
        by = len(b)
        self.res = np.zeros([ax, by])
        print(self.sublcs(a, b))
        print(self.res)

#用动态规划
class Solution(object):
    def lcs(self, a, b):
        lena=len(a)
        lenb=len(b)
        a='0'+a
        b="0"+b
        res=np.zeros([lena+1,lenb+1])
        for i in range(1,lena+1):
            for j in range(1,lenb+1):
                if a[i]==b[j]:
                    res[i][j]=res[i-1][j-1]+1
                else:
                    res[i][j]=max(res[i-1][j],res[i][j-1])
        print(int(res[lena][lenb]))
        self.printlongest(res,a,b)
    def printlongest(self,res,a,b):
        lena=len(a)-1
        lenb=len(b)-1
        while(res[lena][lenb]>0and lena>0 and lenb>0):
            if a[lena]==b[lenb]:
                print(a[lena])
                lena-=1
                lenb-=1
            else:
                if res[lena-1][lenb]==res[lena][lenb]:
                    lena-=1
                    continue
                if res[lena][lenb-1]==res[lena][lenb]:
                    lenb-=1
                    continue

a = "BDCABA"
b = "ABCBDAB"
print(Solution().lcs(a, b))
