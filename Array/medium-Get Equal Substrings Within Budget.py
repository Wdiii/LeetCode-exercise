# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        record=[]
        for i in range(n):
            record.append(abs(ord(t[i])-ord(s[i])))
        left,right=0,0
        tem=0
        res=0
        for right in range(n):
            tem+=record[right]
            while tem>maxCost:
                res=max(res,right-left)
                tem-=record[left]
                left+=1
        res=max(res,right-left+1)
        return res
         