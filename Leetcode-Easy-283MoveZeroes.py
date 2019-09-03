# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
        return nums

print(Solution().moveZeroes([0,1,0,3,12]))



















