# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count=0
        while X<Y:
            count+=1
            if Y%2==0:
                Y//=2
            else:
                Y+=1
        return count+X-Y
     