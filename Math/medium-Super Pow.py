# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def superPow(self, a, b):
        #a: int, b: List[int]) -> int:
        #b % 1337 = (a%1337)^b % 1337
        #xy % 1337 = ((x%1337) * (y%1337)) % 1337
        res=1
        for i in b:
            res=pow(res,10,1337)*pow(a,i,1337)%1337
        return res
        