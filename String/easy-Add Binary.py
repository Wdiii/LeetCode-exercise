# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        nums=int(a,2)+int(b,2)
        #int(x, base)
        ans=bin(nums)
        return ans[2:]