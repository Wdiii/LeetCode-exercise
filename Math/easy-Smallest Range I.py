# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def smallestRangeI(self, A, K):
        # A: List[int], K: int) -> int:
        A.sort()
        if A[-1]-A[0]<=2*K:
            return 0
        else:
            return A[-1]-A[0]-2*K   