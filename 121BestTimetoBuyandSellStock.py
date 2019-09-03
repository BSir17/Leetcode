# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def maxProfit(self, prices) -> int:
        amin=float('inf')
        res=0
        for i in prices:
            if i<amin:
                amin=i
            else:
                if i-amin>res:
                    res=i-amin
        return(res)

print(Solution().maxProfit([7,6,4,3,1]))








