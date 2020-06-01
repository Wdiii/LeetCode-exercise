# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        n=min(n,10)
        if n==0:
            return 1
        dig=9
        res=10
        for i in range(1,n):
            res+=dig*(10-i)
            dig*=10-i  
        return res
            
         