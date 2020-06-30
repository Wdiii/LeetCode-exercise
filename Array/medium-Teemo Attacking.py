# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        #timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0:
            return 0
        res,i=duration,1
        while i<len(timeSeries):
            if timeSeries[i]-timeSeries[i-1]>=duration:
                res+=duration
            else:
                res+=timeSeries[i]-timeSeries[i-1]
            i+=1
        return res
      
class Solution2:
    def findPoisonedDuration(self, timeSeries, duration):    
        res,n = 0,len(timeSeries)
        for i in range(n-1):
            res += min(duration, timeSeries[i+1]-timeSeries[i])
        return res+duration if n>0 else 0
    