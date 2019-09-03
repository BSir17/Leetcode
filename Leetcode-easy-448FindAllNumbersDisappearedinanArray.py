# -*- coding:utf-8 -*-
# Code by Fan.Bai

# 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
class Solution:
    def findDisappearedNumbers(self, nums):
        nums=[0]+nums
        for i in nums:
            if nums[i] > 0 and i>0:
                nums[i] = 0 - nums[i]
            if i<0 and nums[-i]>0:
                nums[-i]=-nums[-i]

        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i)
        return res

print(Solution().findDisappearedNumbers([1,1]))