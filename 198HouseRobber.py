# -*- coding:utf-8 -*-
# Code by Fan.Bai


class Solution:
    def rob(self, nums) -> int:
        res=[]
        amax=0
        if len(nums)==0:
            return 0
        if len(nums)<3:
            return max(nums)
        res.append(nums[0])
        res.append(nums[1])
        res.append(nums[2]+nums[0])
        amax=max(res)
        for i in range(3,len(nums)):
            tmp=nums[i]+max(res[i-2],res[i-3])
            res.append(tmp)
            if tmp>amax:
                amax=tmp
        return amax









