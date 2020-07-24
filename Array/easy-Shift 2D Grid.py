# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def shiftGrid(self, grid, k):
        #grid: List[List[int]], k: int) -> List[List[int]]:
        x=len(grid)
        y=len(grid[0])
        total=x*y
        res=[]
        for i in range(x):
            tem=[]
            for j in range(y):
                num=(i*y+j-k)%total
                m=num//y
                n=num%y
                tem.append(grid[m][n])
            res.append(tem)
        return res
