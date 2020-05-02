# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def addToArrayForm(self, A, K):
        #A: List[int], K: int
        N=int("".join(map(str, A)))
        C=N+K
        return map(int, str(C))
     
