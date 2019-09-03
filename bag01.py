# -*- coding:utf-8 -*-
# Code by Fan.Bai

import numpy as np



# w = [0, 2, 3, 4, 5]
# v = [0, 3, 4, 5, 6]
# s = 8
# n = 4



class Solution:
    def bag(self, n,s,w,v):
        res = [0] * (s + 1)
        res = [res] * (n + 1)

        res = np.array(res)
        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if w[i] > j:
                    res[i][j] = res[i - 1][j]
                else:
                    res[i][j] = max([res[i - 1][j], res[i - 1][j - w[i]] + v[i]])
        print(res)

        #选择最大的结果
        amax=0
        loci=locj=0
        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if res[i][j]>amax:
                    amax=res[i][j]
                    loci=i
                    locj=j
        # 打印选择了哪些物品
        while loci>0 and locj>0:
            if res[loci][locj]==res[loci-1][locj]:
                loci=loci-1
                continue
            if res[loci][locj]==res[loci-1][locj-w[loci]]+v[loci]:
                print(w[loci],v[loci])
                locj -= w[loci]
                loci-=1






class Solution1:
    def bag(self, n,s,w,v):
        res = [0] * (s + 1)
        res=np.array(res)
        for i in range(1, n + 1):
            for j in range(s,0,-1):
                if j>w[i]:
                    res[j]=max(res[j],res[j-w[i]]+v[i])

        print(res)

n=int(input())
s=int(input())
w=[0]
v=[0]
for i in range(n):
    ss=str(input())
    w.append(int(ss.split()[0]))
    v.append(int(ss.split()[1]))

Solution().bag(n,s,w,v)
