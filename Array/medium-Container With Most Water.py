# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxArea(self, height):
        #height: List[int]) -> int:
        n=len(height)-1
        i=0
        res=0
        while i<n:
            res=max(res,min(height[i],height[n])*(n-i))
            if (height[i] < height[n]):
                i+=1
            else:
                n-=1
        return res 
            
