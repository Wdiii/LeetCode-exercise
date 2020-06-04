# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        dig=1
        while n>dig*9*10**(dig-1):
            n-=dig*9*10**(dig-1)
            dig+=1
        a=(n-1)//dig
        b=(n-1)%dig
        num=10**(dig-1)+a
        res=str(num)[b]
        return int(res)
    