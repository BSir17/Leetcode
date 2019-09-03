# -*- coding:utf-8 -*-
# Code by Fan.Bai

#左右两遍动态规划解决
class Solution:
    def productExceptSelf(self, nums):
        alen=len(nums)
        left=[]
        right=[]
        left.append(1)
        right.append(1)
        for i in range(1,len(nums)):
            left.append(nums[i-1]*left[i-1])
        for i in range(len(nums)-1)[::-1]:
            right.append(nums[i+1]*right[alen-i-2])
        res=[]
        alen=len(left)
        for i in range(alen):
            res.append(left[i]*right[alen-1-i])
        return res

print(Solution().productExceptSelf([]))















