# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        else:
            count=1
            l=2
            while l<num//l:
                if num%l==0:
                    count=count+l+num//l
                l+=1
            return count==num