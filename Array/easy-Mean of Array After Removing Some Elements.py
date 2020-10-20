# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def trimMean(self, arr):
        #arr: List[int]) -> float:
        remove=len(arr)//20
        return sum(sorted(arr)[remove:-remove])/(len(arr)-remove*2)
        