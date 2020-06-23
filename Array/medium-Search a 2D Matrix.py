# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 02:42:24 2020

@author: Di Wang
"""

class Solution:
    def searchMatrix(self, matrix, target):
        #matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        i=0
        while i<len(matrix):
            if target>matrix[i][-1]:
                i+=1
            else:
                break
        if i<len(matrix):
            return target in matrix[i]
        else:
            return False
        