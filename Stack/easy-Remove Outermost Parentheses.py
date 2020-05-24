# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res=""
        count=0
        for i in S:
            if i=="(":
                count+=1
                if count!=1:
                    res+=i
            else:
                count-=1
                if count!=0:
                    res+=i
        return res
