# -*- coding: utf-8 -*-  
#3. 无重复字符的最长子串
#https://blog.csdn.net/ssswill/article/details/86683311
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        temp=""
        maxnum=0
        for i in range(0,len(s)):
            if s[i] in temp:
                alen=len(temp)
                if alen>maxnum:
                    maxnum=alen
                start =temp.index(s[i])+1
                temp=temp[start:]+s[i]

            else:
                temp+=s[i]
                if len(temp)>maxnum:
                    maxnum=len(temp)
        return maxnum

#https://www.cnblogs.com/Lin-Yi/p/9600990.html
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        d={}
        maxlen=0
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]<start:
                    d[s[i]]=i
                    tmpmax=i-start+1
                    if tmpmax>maxlen:
                        maxlen=tmpmax
                else:
                    tmpmax =i-start
                    if tmpmax>maxlen:
                        maxlen=tmpmax
                    start=d[s[i]]+1
                    d[s[i]]=i
            else:
                d[s[i]]=i
                tmpmax=i-start+1
                if tmpmax > maxlen:
                    maxlen = tmpmax
        return maxlen

ss="abcabcbbab"
#ss="bbbbb"
print(Solution().lengthOfLongestSubstring(ss))