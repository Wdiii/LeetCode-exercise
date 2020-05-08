# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A")>1:
            return False
        else:
            count=0
            for i in s:
                if i=="L" and count==2:
                    return False
                elif i=="L":
                    count+=1
                else:
                    count=0
        return True