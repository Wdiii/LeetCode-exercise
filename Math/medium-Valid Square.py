# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        #p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def d(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        s = set([d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)])
        return 0 not in s and len(s) == 2
