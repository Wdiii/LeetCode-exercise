# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def fib(self, N):
        value=[0,1]
        for i in range(2,N+1):
            value.append(value[i-1]+value[i-2])
        return value[N]