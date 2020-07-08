# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import Counter
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        a,b=0,0
        dicS=Counter(S)
        result=dicS["0"]
        for s in S:
            if s=='1':
                a+=1
            else:
                b+=1
            result=min(result,a+dicS["0"]-b)
        return result
    