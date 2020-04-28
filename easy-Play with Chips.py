# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def minCostToMoveChips(self, chips):
        # chips: List[int]) -> int:
        odd,even = 0,0
        for i in chips:
            if i%2==0:
                even+=1
            else:
                odd+=1
        if even>=odd:
            return odd
        else:
            return even