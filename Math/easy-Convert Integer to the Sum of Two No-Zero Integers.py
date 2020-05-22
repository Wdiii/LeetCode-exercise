# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
           
class Solution:
    def getNoZeroIntegers(self, n):
        #n: int) -> List[int]:
        a=1
        while "0" in str(a) or "0" in str(n-a):
            a+=1
        return [a,n-a] 
