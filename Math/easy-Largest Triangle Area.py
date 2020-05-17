# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def largestTriangleArea(self, points):
        #points: List[List[int]]) -> float:
        #S=(1/2)*abs(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
        s, res = 0,0
        n=len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    s=abs(points[i][0]*points[j][1]+points[j][0]*points[k][1]+points[k][0]*points[i][1]-points[i][0]*points[k][1]-points[j][0]*points[i][1]-points[k][0]*points[j][1])/2
                    res=max(res,s)
        return res