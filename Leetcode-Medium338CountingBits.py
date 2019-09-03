# -*- coding:utf-8 -*-
# Code by Fan.Bai

class Solution:
    def countBits(self, num: int):
        res = []
        res.append(0)
        res.append(1)
        res.append(1)
        base = 1
        alen = 3
        while (num > alen):
            for i in range(1, 2 ** base ):
                res.append(res[2 ** base] + res[i])
                alen += 1
            res.append(1)
            base+=1
        return res[:num+1]


print(Solution().countBits(5))
