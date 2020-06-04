# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def integerReplacement(self, n: int) -> int:
        count=0
        while n!=1:
            count+=1
            if n%2==0:
                n=n//2
            else:
                if n&2 and n!=3:
                    n+=1
                else:
                    n-=1
        return count
#bin(5)='0b101', 5&2=0, bin(7)='0b111',7&2=2, end with 11, +1, 01, -1
