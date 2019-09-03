# -*- coding:utf-8 -*-
# Code by Fan.Bai

# 用动规来找有多少种方法
def find_num(target, s):
    # res[i]代表达到容量为i共有多少种方法
    res = [0] * (target + 1)
    for i in s:
        for j in range(target, i - 1, -1):
            if j == i:
                res[j] += 1
            else:
                res[j] += res[j - i]
    return res[target]


# 用回溯法来寻找组合数
class Solution():
    def findtar(self, target, s):
        self.totalsolusum = 0
        s.sort()
        self.huisu(s, 0, 0, target)
        return self.totalsolusum

    def huisu(self, s, loc, presum, target):
        if presum+s[loc]>target:
            return
        if presum+s[loc]<target:
            self.huisu(s,loc+1,presum+s[loc],target)
            self.huisu(s,loc+1,presum,target)
        if presum+s[loc]==target:
            self.totalsolusum+=1
            return 1

## 用回溯法来寻找合法的组合，并打印
class Solution1():
    def findtar(self, target, s):
        self.totalsolusum = 0
        self.res=[]
        s.sort()
        tmp=[0]*len(s)
        self.huisu(s, 0, 0, target,tmp)
        return self.totalsolusum,self.res

    def huisu(self, s, loc, presum, target,usedrec):
        if presum+s[loc]>target:
            return
        if presum+s[loc]<target:
            self.huisu(s, loc + 1, presum, target,usedrec+[])
            usedrec[loc]=1
            self.huisu(s,loc+1,presum+s[loc],target,usedrec+[])
        if presum+s[loc]==target:
            self.totalsolusum+=1
            usedrec[loc]=1
            self.res.append(usedrec)
            return

s = [1, 2, 3, 4, 5,6,7,8,9,10]

target = 10
# print(find_num(target, s))
num,res=Solution1().findtar(10,s)
print(num)
print(res)