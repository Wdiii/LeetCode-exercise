# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        test=1
        lstN,lstU=[],[]
        while len(lstU)!=n:
            num=test
            while num!=1:
                if num%2==0:
                    num=num//2
                elif num%3==0:
                    num=num//3
                elif num%5==0:
                    num=num//5
                else:
                    lstN.append(num)
                    
            lstU.append(test)
            test+=1
        return lstU.pop()

#this solution will run out of time, so we need to improve it.

class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return False
        t1 = 0
        t2 = 0
        t3 = 0
        res = [1]
        while len(res) < n:
            res.append(min(res[t1]*2, res[t2]*3, res[t3]*5))
            if res[-1] == res[t1]*2:
                t1 += 1
            if res[-1] == res[t2]*3:
                t2 += 1
            if res[-1] == res[t3]*5:
                t3 += 1
        return res.pop()
