# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return "i"*(n-1)+"j"
        return "i"*n