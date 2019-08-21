# -*- coding:utf-8 -*-
# Code by Fan.Bai
import copy
#思路1，设置一个访问数组，表示该数字是否已经被加入到了暂存结果中，没被加入的可以被加入，暂存结果长度符合条件，加到结果集合，返回上一个位置
#需要pop出来
class Solution1:
    def outputone(self,nums,nowlen):
        for i in range(len(nums)):
            if self.visited[i]==0:
                self.tmpres.append(nums[i])
                self.visited[i]=1

                if nowlen==len(nums):
                    #tmp=[str(i)for i in self.tmpres]
                    self.res.append(copy.copy(self.tmpres))
                    self.visited[i]=0
                    self.tmpres.pop(-1)
                    return
                else:
                    self.outputone(nums,nowlen+1)
                    self.visited[i]=0
                    self.tmpres.pop(-1)



    def permute(self, nums):
        self.tmpres=[]
        self.res=[]
        alen=len(nums)
        self.visited=[0]*alen
        self.outputone(nums,1)
        return self.res
#思路一样，只是进行了优化，都是对第i个值进行遍历，稍有不同的是，这里的思想是
#长度为i+1的全拍列可以看做，第1位加上剩余的全排列

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==None:
            return []
        if len(nums)==1:
            return [[nums[0]]]
        else:
            res=[]
            for i in nums:
                numms=nums+[]
                numms.remove(i)
                tmpres=self.permute(numms)
                for j in tmpres:
                    res.append([i]+j)
            return res


tmp=[1,2,3]
print(Solution().permute(tmp))

tmm=tmp+[]
