# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isBoomerang(self, points):
        #points: List[List[int]]) -> bool:
        a,b,c=points
        a1,a2=a
        b1,b2=b
        c1,c2=c
        if a==b or b==c or a==c:
            return False
        else:
            return (a1-b1)*(a2-c2)!=(a1-c1)*(a2-b2)