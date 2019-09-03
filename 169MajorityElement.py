# -*- coding:utf-8 -*-
# Code by Fan.Bai


class Solution:
    def majorityElement(self, nums) -> int:
        num=1
        rec=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==rec:
                num+=1
            else:
                num-=1
                if num==0:
                    rec=nums[i]
                    num+=1
        return rec







