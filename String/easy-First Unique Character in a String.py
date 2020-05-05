# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst=list(s)
        dic={}
        for i in lst:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        res=-1
        for j in range(len(lst)):
            if dic[lst[j]]==1:
                res=j
                break
        return res
            