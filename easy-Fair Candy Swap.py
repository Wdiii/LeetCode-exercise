# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def fairCandySwap(self, A, B):
        b = set(B)
        middle = ((sum(B)-sum(A)))//2
        for ele in A:
            if middle+ele in b:
                return [ele,middle+ele]  