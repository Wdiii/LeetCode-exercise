# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def generate(self, numRows):
        #numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        res=[]
        for i in range(numRows):
            res.append([1])
            for j in range(1,i+1):
                if i==j:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j]+res[i-1][j-1])
        return res
                    