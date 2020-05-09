# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if s.count("0")==0 or s.count("1")==0:
            return 0
        count=0
        a="01"
        b="10"
        while a in s or b in s:
            count+=s.count(a)+s.count(b)
            a="0"+a+"1"
            b="1"+b+"0"
        return count
    
#time limit exceeded
#after adjustment

class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        if s.count("0")==0 or s.count("1")==0:
            return 0
        s=s.replace("01","0 1")
        s=s.replace("10","1 0")
        s=s.split(" ")
        count=0
        for i in range(len(s)-1):
            count+=min(len(s[i]),len(s[i+1]))
        return count