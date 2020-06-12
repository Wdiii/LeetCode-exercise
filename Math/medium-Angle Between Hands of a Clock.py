# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m=minutes/60*360
        h=(hour%12+minutes/60)/12*360
        res=min(abs(m-h),abs(h-m))
        if res<=180:
            return res
        else:
            return 360-res
        
#solution from leetcode 80% | 100% 
class Solution1:
    def angleClock(self, hour: int, minutes: int) -> float: 
        return min(360-abs((hour * 30 + minutes * 0.5) - (minutes * 6)),
                   abs((hour * 30 + minutes * 0.5) - (minutes * 6)))