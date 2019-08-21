# -*- coding:utf-8 -*-
# Code by Fan.Bai

#用个栈就完事了
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        dict={}
        dict['(']=')'
        dict['{']='}'
        dict['[']="]"
        mystack=[]
        if s[0] not in dict:
            return False
        mystack.append(s[0])
        for i in range(1,len(s)):
            if s[i] in dict:
                mystack.append(s[i])
            else:
                if len(mystack)>0 and s[i]==dict[mystack[-1]]:
                    mystack.pop(-1)
                else:
                    return False
        if len(mystack)>0:
            return False
        return True

print(Solution().isValid("[])"))