# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        lst1=list(num1)
        lst2=list(num2)
        sum1,sum2=0,0
        for i in lst1:
            sum1=sum1*10+int(i)
        for j in lst2:
            sum2=sum2*10+int(j)
        return str(sum1+sum2)
            