# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        a=bin(N)
        b="0b"
        for i in range(2,len(a)):
            if a[i]=="0":
                b+="1"
            else:
                b+="0"
        return int(b,2)
