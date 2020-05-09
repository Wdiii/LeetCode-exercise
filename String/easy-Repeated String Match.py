# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        b=len(B)//len(A)+1
        for i in range(1,b+2):
            if B in i*A:
                return i
        return -1