# -*- coding:utf-8 -*-
# Code by Fan.Bai


#https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-dong-tai-gui-hua-by-jy/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if len(p)>1 and p[1]=='*':
            if s and  (p[0]=='.'or p[0]==s[0]) :
                return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
            else:return self.isMatch(s,p[2:])
        if s and (p[0]=='.' or s[0]==p[0]):
            return self.isMatch(s[1:],p[1:])
        return False

s = 'aa'
p = 'a*'
print(Solution().isMatch(s, p))
