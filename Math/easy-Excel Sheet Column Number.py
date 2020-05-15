# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        n=len(s)-1
        i=0
        res=0
        while i<=n:
            res=(ord(s[i])-64)*26**(n-i)+res
            i+=1
        return res