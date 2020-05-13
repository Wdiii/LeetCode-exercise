# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def sortString(self, s: str) -> str:
        lst=list(s)
        res=[]
        while len(lst)>=1:
            a=list(set(lst))
            a.sort()
            for i in a:
                res.append(i)
                lst.remove(i)
            b=list(set(lst))
            b.sort(reverse=True)
            for j in b:
                res.append(j)
                lst.remove(j)
        return "".join(res)