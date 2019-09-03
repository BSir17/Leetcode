# -*- coding:utf-8 -*-
# Code by Fan.Bai


# 两数之和的扩展版本
class Solution:
    def threeSum(self, nums):
        if len(nums) < 1:
            return None
        myset = set()
        for i in range(len(nums)):
            alist = nums + []
            del (alist[i])
            adict = {}
            tar = 0 - nums[i]
            for j in range(0, len(alist)):
                if alist[j] in adict:
                    rest = adict[alist[j]]
                    tmpres = [nums[i], alist[j], rest]
                    tmpres.sort()
                    myset.add(tuple(tmpres))
                else:
                    adict[tar - alist[j]] = alist[j]
            res = []
        for i in myset:
            res.append(list(i))
        return res


# 拍好序号的数组中找和的办法
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            success = []
            alist = nums + []
            del (alist[i])
            tar = 0 - nums[i]
            head = 0
            tail = len(alist) - 1
            while head < tail:
                if alist[head] + alist[tail] == tar:
                    res.append([nums[i], alist[head], alist[tail]])
                    head += 1
                    tail -= 1
                elif alist[head] + alist[tail] < tar:
                    head += 1
                else:
                    tail -= 1
        return list(set((tuple(sorted(i))for i in res)))



print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
