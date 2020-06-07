# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def reachNumber(self, target: int) -> int:
        t=abs(target)
        k=0
        s=0
        while s<t:
            k+=1
            s+=k
        dt=s-t
        if dt%2==0:
            return k
        else:
            if k%2==0:
                return k+1
            else:
                return k+2 