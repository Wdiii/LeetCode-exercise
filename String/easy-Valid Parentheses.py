# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        else:
            while len(s)>1:
                ori=len(s)
                i=0
                while i < len(s)-1:
                    if s[i]=="[" and s[i+1]=="]" or s[i]=="{" and s[i+1]=="}" or s[i]=="(" and s[i+1]==")":
                        s=s.replace(s[i:i+2],"")
                        i=0
                    else:
                        i+=1
                if len(s)==ori:
                    break
            if s=="":
                return True
            else:
                return False

#not fast, need to improve
