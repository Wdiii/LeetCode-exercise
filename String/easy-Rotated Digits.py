# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        count=0
        for i in range(1,N+1):
            n=str(i)
            if n.count("3")+n.count("4")+n.count("7")==0:
                if n.count("1")+n.count("8")+n.count("0")!=len(n):
                    count+=1
        return count
        