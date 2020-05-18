# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def binaryGap(self, N: int) -> int:
        a=bin(N)
        count=0
        dis=0
        for i in range(len(a)):
            if a[i]=="1":
                count+=1
                if count==2:
                    dis=max(dis,i-tem)
                    count=1
                tem=i
        return dis
