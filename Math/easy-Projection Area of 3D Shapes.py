# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def projectionArea(self, grid):
        #grid: List[List[int]]) -> int:
        x,y,z=0,0,0
        n=len(grid)
        for i in range(n):
            a,b=0,0
            for j in range(n):
                if grid[i][j]!=0:
                    z+=1
                a=max(a,grid[i][j])
                b=max(b,grid[j][i])
            x+=a
            y+=b
        return x+y+z