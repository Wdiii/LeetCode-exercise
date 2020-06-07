# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        n1=list(str(num))
        n2=list(str(num))
        n2.sort(reverse=True)
        if n1==n2:
            return num
        else:
            for i in range(len(n1)):
                if n1[i]!=n2[i]:
                    for j in range(len(n1)-1,-1,-1):
                        if n1[j]==n2[i]:
                            n1[j]=n1[i]
                            n1[i]=n2[i]
                            break
                    else:
                        j-+1
                    break
                else:
                    i+=1
            return int("".join(n1))