# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def clumsy(self, N: int) -> int:
        if N==1:
            return 1
        elif N==2:
            return 2
        elif N==3:
            return 6
        else:
            res=N*(N-1)//(N-2)+(N-3)
            N-=4
            while N>=4:
                tem=N*(N-1)//(N-2)
                res-=tem-(N-3)
                N-=4
            if N==1:
                res-=1
            if N==2:
                res-=2
            if N==3:
                res-=6
            return res