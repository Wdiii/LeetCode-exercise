# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        #left: int, right: int) -> List[int]:
        i=left
        res=[]
        while i<=right:
            if "0" not in str(i):
                for j in range(len(str(i))):
                    if i%int(str(i)[j])==0:
                        j+=1
                    else:
                        break
                if j==len(str(i)):
                    res.append(i)
            i+=1
        return res