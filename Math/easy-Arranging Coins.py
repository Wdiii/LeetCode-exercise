# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<2:
            return n
        else:
            i=1
            count=0
            while count<=n:
                count+=i
                i+=1
            return i-2