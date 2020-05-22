# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
           
class Solution:
    def findSolution(self, customfunction, z):
        #customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x,y=1,1000
        res=[]
        while x<=1000 and y>=1:
            tem=customfunction.f(x,y)
            if tem<z:
                x+=1
            elif tem>z:
                y-=1
            else:
                res.append([x,y])
                x+=1
        return res