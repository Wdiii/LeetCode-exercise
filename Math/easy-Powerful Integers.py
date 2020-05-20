# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def powerfulIntegers(self, x, y, bound):
        # x: int, y: int, bound: int) -> List[int]:
        a,b=0,0
        res=[]
        if x==1 and y==1:
            if bound>=2:
                res.append(2)
        elif x==1:
            while y**b+1<=bound:
                res.append(y**b+1)
                b+=1
        elif y==1:
            while x**a+1<=bound:
                res.append(x**a+1)
                a+=1
        else:  
            while x**a+1<=bound:
                if x**a+y**b<=bound:
                    res.append(x**a+y**b)
                    b+=1
                else:
                    a+=1
                    b=0
        return list(set(res))
      
#easier way
class Solution1:
    def powerfulIntegers(self, x, y, bound):
        i = 0
        j = 0
        A = set()
        x, y = max(x,y), min(x,y)
        while x**i + y**j <= bound:
            if x == 1:
                return [2]
            if y == 1:
                A.add(x**i+1)
            else:
                while x**i + y**j <= bound:
                    A.add(x**i+y**j)
                    j+=1
            i+=1
            j=0
        return list(A)
      
