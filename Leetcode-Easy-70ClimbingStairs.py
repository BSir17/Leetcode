# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def climbStairs(self, n: int) -> int:
        res=[0,1,2,3]
        if n<4:
            return res[n]
        for i in range(4,n+1):
            res.append(res[i-1]+res[i-2])
        return res[-1]

print(Solution().climbStairs(4))