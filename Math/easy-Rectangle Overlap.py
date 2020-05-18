# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        #rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return (x4-x1)*(x3-x2)<0 and (y4-y1)*(y3-y2)<0
        