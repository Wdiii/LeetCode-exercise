# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
           
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        N=str(n)
        S,P=0,1
        for i in N:
            S+=int(i)
            P*=int(i)
        return P-S