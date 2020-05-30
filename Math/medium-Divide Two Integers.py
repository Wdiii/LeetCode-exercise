# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:24:40 2020

@author: Di Wang
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend*divisor>0:
            res=abs(dividend)//abs(divisor)
        else:
            res=-(abs(dividend)//abs(divisor))
        intmin=-(2**31)
        intmax=(2**31)-1
        return res if intmin<=res<=intmax else intmax

#pay attention!
#Assume we are dealing with an environment which could only store integers within
#the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
#For the purpose of this problem, assume that your function returns (2**31)−1 
#when the division result overflows.