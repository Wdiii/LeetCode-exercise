# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def simplifiedFractions(self, n):
        #n: int) -> List[str]:
        def gcd(l,s):
            if l%s==0:
                return s
            else:
                return gcd(s,l%s)   
        if n==1:
            return []
        res=[]
        while n>=2:
            for i in range(1,n):
                if gcd(n,i)==1:
                    res.append(str(i)+"/"+str(n))
            n-=1
        return res
