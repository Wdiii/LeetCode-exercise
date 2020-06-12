# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        #tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices%2!=0:
            return []
        elif tomatoSlices>cheeseSlices*4 or tomatoSlices<cheeseSlices*2:
            return []
        else:
            a=tomatoSlices-cheeseSlices*2
            if a%2!=0:
                return []
            else:
                return [a//2,cheeseSlices-a//2]
            