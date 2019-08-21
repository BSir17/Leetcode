# -*- coding: utf-8 -*-  
# 1.两数之和
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                target = [d[nums[i]], i]
                return target
            else:
                d[target-nums[i]]=i

nums=[2, 7, 11, 15]
print(Solution().twoSum(nums,9))