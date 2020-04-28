# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def sumZero(self, n):
        #n: int) -> List[int]:
        a=n//2
        if n == 1:
            lst=[0]
        elif n%2 == 0:
            lst=[]
            while a>0:
                lst.append(-a)
                lst.append(a)
                a-=1
        else:
            lst=[0]
            while a>0:
                lst.append(-a)
                lst.append(a)
                a-=1
        return lst
        