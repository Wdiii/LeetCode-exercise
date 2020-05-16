# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:       
        l,r=1,num//2
        while l<r:
            m=(l+r)//2
            if m*m<num:
                l=m+1
            elif m*m>num:
                r=m-1
            else:
                return True
        if l*l==num:
            return True
        else:
            return False