# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution(object):
    def subsets(self, nums):
        res=[[]]
        for i in nums:
            ress=res+[]
            for j in ress:
                res.append(j+[i])
        return res


print(Solution().subsets([1,2,3]))











