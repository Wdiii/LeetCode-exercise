# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

A=[[1,2,3],[4,5,6],[7,8,9]]
class Solution:
    def transpose(self, A):
        row=len(A)
        col=len(A[0])
        return [[A[r][c] for r in range(row)] for c in range(col)]

#or
class Solution2:
    def transpose(self, A):
        return [n for n in zip(*A)]