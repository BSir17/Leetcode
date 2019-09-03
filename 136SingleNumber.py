# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def singleNumber(self, nums) -> int:
        res=0
        for i in nums:
            res=res^i
        return res


