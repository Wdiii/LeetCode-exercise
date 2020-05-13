# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def stringMatching(self, words):
        #words: List[str]) -> List[str]:
        res=[]
        for i in words:
            a=words.copy()
            a.remove(i)
            for j in a:
                if i in j:
                    res.append(i)
                    break
        return res