# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def setZeroes(self, matrix):
        #matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col=len(matrix[0])
        row=len(matrix)
        a,b=[],[]
        for i,line in enumerate(matrix):
            #print(list(enumerate(matrix)))
            for x in range(len(line)):
                if line[x] == 0:
                    if x not in b:
                        b.append(x)
                    if i not in a:
                        a.append(i)
        for m in a:
            matrix[m] = [0]*col
        for n in b:
            for r in range(row):
                matrix[r][n]=0
                