# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:34:40 2020

@author: Di Wang
"""

class Solution:
    def isMonotonic(self, A):
        F=sorted(A)
        B=F[::-1]
        return (A==F or A==B)


#one line
def isMonotonic(self, A):
    return A==sorted(A) or A==sorted(A)[::-1]