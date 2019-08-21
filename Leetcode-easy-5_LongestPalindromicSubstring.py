# -*- coding: utf-8 -*-
#5. 最长回文子串,两种方法，一种是中心辐射法则，o(n^2),一种动态规划，一种是马拉车法o(n)
#以下是中心辐射法
def countji(s,i):
    alen=len(s)
    loc=1
    while(i+loc<alen and i-loc>=0 and s[i+loc]==s[i-loc]):
        loc+=1
    loc-=1
    return loc*2+1

def countlou(s,i):
    alen=len(s)
    l=i-1
    r=i
    loc=1
    while(l-loc>=0 and r+loc<alen and s[l-loc]==s[r+loc]):
        loc+=1
    loc-=1
    return 2+loc*2


def countrou(s,i):
    alen = len(s)
    l = i
    r = i+1
    loc = 1
    while (l - loc >= 0 and r + loc < alen and s[l - loc] == s[r + loc]):
        loc += 1
    loc -= 1
    return 2 + loc * 2

def getmax(*a):
    maxx=a[0]
    for i in a :
        if i>maxx:
            maxx=i
    return maxx

class Solution:
    def longestPalindrome(self, s: str):
        alen=len(s)
        if alen<=1:
            return s
        elif alen==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        maxrec=[]
        maxstr=[]
        for i in range(1,len(s)-1):
            ji=1
            lou=1
            rou=1
            if s[i-1]==s[i+1]:
                ji=countji(s,i)
            if s[i-1]==s[i]:
                lou=countlou(s,i)
            if s[i+1]==s[i]:
                rou=countrou(s,i)
            maxx=getmax(ji,lou,rou)
            maxrec.append(maxx)
            if maxx==1:
                maxstr.append(s[i])
                continue
            if maxx==ji:
                maxstr.append(s[i-(maxx-1)//2:i+(maxx-1)//2+1])
            elif maxx==lou:
                maxstr.append(s[i - (maxx) // 2:i + (maxx) // 2 ])
            else:
                maxstr.append(s[i - (maxx) // 2+1:i + (maxx) // 2+1])
        return maxstr[maxrec.index(max(maxrec))]


s=""
print(Solution().longestPalindrome(s))























