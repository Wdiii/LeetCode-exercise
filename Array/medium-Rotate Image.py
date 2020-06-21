# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def rotate(self, matrix):
        #matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            n=len(matrix)
            for i in range(n//2):
                for j in range(n):
                    matrix[i][j],matrix[n-i-1][j]=matrix[n-i-1][j],matrix[i][j]
            for k in range(n):
                for l in range(k):
                    matrix[k][l],matrix[l][k]=matrix[l][k],matrix[k][l]
