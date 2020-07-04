# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isOneBitCharacter(self, bits):
        #bits: List[int]) -> bool:
        i=0
        while i<len(bits):
            if i==len(bits)-1:
                return bits[i]==0
            else:
                if bits[i]==1:
                    i+=2
                else:
                    i+=1
        return False