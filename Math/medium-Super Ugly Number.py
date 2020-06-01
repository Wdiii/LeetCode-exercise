# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        #: int, primes: List[int]) -> int:
        res=[1]
        t=[0]*len(primes)
        while len(res)<n:
            m = pow(2, 32)
            for i in range(len(primes)):
                tem=primes[i]*res[t[i]]
                if tem<m:
                    m=tem
            for j in range(len(primes)):
                if m== res[t[j]] * primes[j]:
                    t[j] += 1
            res.append(m)    
        return res.pop()
    