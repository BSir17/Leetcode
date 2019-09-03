# -*- coding:utf-8 -*-
# Code by Fan.Bai

import numpy as np


# 最长公共字串和最长公共子序列很类似
# 递归方法，res[i][j]代表以i和j结尾的最长公共字串长度
class Solution1(object):
    def sublcs(self, a, b):
        lena = len(a)
        lenb = len(b)
        if len(a) == 0 or len(b) == 0:
            return 0
        if a[-1] == b[-1]:
            pres = self.sublcs(a[:-1], b[:-1])
            self.res[lena - 1][lenb - 1] = pres + 1
        else:
            pres = max([self.sublcs(a[:-1], b), self.sublcs(a, b[:-1])])
            self.res[lena - 1][lenb - 1] = 0

        return self.res[lena - 1][lenb - 1]

    def lcs(self, a, b):
        ax = len(a)
        by = len(b)
        self.res = np.zeros([ax, by])
        self.sublcs(a, b)
        print(self.res)


# 动态规划方法
class Solution(object):
    def lcs(self, a, b):
        lena = len(a)
        lenb=len(b)
        res=np.zeros([lena+1,lenb+1])
        a="0"+a
        b="0"+b
        for i in range(1,lena+1):
            for j in range(1,lenb+1):
                if a[i]==b[j]:
                    res[i][j]=res[i-1][j-1]+1
        print(res)

a = "helloworld"
b = "lowop"
Solution().lcs(a, b)
