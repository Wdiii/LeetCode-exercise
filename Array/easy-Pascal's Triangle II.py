# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def getRow(self, rowIndex):
        # rowIndex: int) -> List[int]:
        res=[1]
        if rowIndex==0:
            return res
        for i in range(1,rowIndex+1):
            res=[1]+[res[i]+res[i+1] for i in range(len(res)-1)]+[1]
        return res
    