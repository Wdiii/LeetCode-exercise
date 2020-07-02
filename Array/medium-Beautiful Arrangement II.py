# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def constructArray(self, n, k):
        # n: int, k: int) -> List[int]:
        res=list(range(1,n+1))
        for i in range(1,k):
            res[i:]=res[:i-1:-1]
        return res
        