# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def oddCells(self, n, m, indices):
        #n: int, m: int, indices: List[List[int]]) -> int:
        res=[[0]*m for i in range(n)]
        for r,c in indices:
            for j in range(n):
                res[j][c]+=1
            for k in range(m):
                res[r][k]+=1
        count=0
        for a in range(n):
            for b in range(m):
                if res[a][b]%2:
                    count+=1
        return count
