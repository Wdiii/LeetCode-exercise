# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if i in dic:
                dic[i]+=1
        return min(dic["b"],dic["a"],dic["l"]//2,dic["o"]//2,dic["n"])