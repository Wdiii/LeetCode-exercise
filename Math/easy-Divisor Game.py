# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2==0
    
#if N is odd, Alice can only select odd, then Bob can choose -1 each time,
#finally Bob can get 2 then Bob wins.