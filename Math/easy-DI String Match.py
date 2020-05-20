# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def diStringMatch(self, S):
        #S: str) -> List[int]:
        a,b=0,len(S)
        lst=[]
        for i in range(len(S)):
            if S[i]=="I":
                lst.append(a)
                a+=1
            else:
                lst.append(b)
                b-=1
        if S[-1]=="I":
            lst.append(a)
        else:
            lst.append(b)
        return lst