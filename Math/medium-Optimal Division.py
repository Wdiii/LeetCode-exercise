# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def optimalDivision(self, nums):
        #nums: List[int]) -> str:
        n=list(map(str,nums)) #convert list to string
        if len(n)<=2:
            return "/".join(n)
        return "{}/({})".format(n[0],"/".join(n[1:]))
