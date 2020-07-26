# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countServers(self, grid):
        #grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    for r in range(row):
                        if r!=i:
                            if grid[r][j] in [1,2]:
                                grid[i][j]=2
                                grid[r][j]=2
                    for c in range(col):
                        if c!=j:
                            if grid[i][c] in [1,2]:
                                grid[i][j]=2
                                grid[i][c]=2
                if grid[i][j]==2:
                    count+=1
        return count                    
        