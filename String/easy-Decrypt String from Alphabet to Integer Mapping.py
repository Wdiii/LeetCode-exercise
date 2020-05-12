# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result=""
        i=0
        while i < len(s)-2:
            if s[i+2]=="#":
                result+=chr(int(s[i:i+2])+96)
                i+=3
            else:
                result+=chr(int(s[i])+96)
                i+=1
        while i < len(s):
            result+=chr(int(s[i])+96)
            i+=1
        return result

#use python chr() from number -> char | ord() from char -> number with ASCII 