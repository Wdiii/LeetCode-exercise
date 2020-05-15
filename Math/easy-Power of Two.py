# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n>1:
            n=n/2
        return n==1.0