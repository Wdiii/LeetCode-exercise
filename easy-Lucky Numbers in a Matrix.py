# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def luckyNumbers (self, matrix):
        #matrix: List[List[int]]) -> List[int]:
        result=[]
        m=len(matrix)
        n=len(matrix[0])
        lst = sum(matrix, [])
        for i in range(m):
            a=min(matrix[i])
            j=matrix[i].index(a)
            b=max(lst[j::n])
            if a == b:
                result.append(a)
        return result

#matrix to list, I use "lst = sum(matrix, [])",which is important for this solution