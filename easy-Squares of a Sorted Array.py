# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def sortedSquares(self, A):
        lst=[]
        for ele in A:
            lst.append(ele*ele)
        return sorted(lst)
        