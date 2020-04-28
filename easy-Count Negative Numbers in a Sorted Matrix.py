# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countNegatives(self, grid):
        #grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        return count