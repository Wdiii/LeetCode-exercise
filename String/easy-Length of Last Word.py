# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="":
            return 0
        else:
            count=0
            i=len(s)-1
            j=i
            while i>=0:
                if s[i]==" ":
                    i-=1
                else:
                    j=i
                    break
            while j>=0:
                if s[j]!=" ":
                    count+=1
                    j-=1
                else:
                    break
            return count

#other solution from leetcode
def lengthOfLastWord(self, s):
        if len(s)==0:
            return 0
        t = s.strip().split(" ")
        return len(t[-1])        