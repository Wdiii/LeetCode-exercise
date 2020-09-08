# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def threeConsecutiveOdds(self, arr):
        #arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i=0
        while i<=len(arr)-3:
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                return True
                break
            else:
                i+=1
        return False
     
class Solution2:
    def threeConsecutiveOdds(self, arr):
        count=0
        for i in arr:
            if i%2==1:
                count+=1
                if count==3:
                    return True
            else:
                count = 0
        return False
    