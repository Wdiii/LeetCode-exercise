# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #total m+n-2 steps
        res = 1
        for i in range(m, m+n-1):
            res*=i
            res//=i-m+1
        return res
#in this question, you want to get C(n-1)(m+n-2)   