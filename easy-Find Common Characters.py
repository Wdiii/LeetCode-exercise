# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def commonChars(self, A):
        #A: List[str]) -> List[str]:
        n=len(A)
        ans=[]
        for ele in A[0]:
            i=0
            while i<n-1:
                if ele not in A[i+1]:
                    break
                else:
                    lst=list(A[i+1]) #want to remove this element,so we need to have a list
                    p=lst.index(ele)
                    del(lst[p])
                    A[i+1]="".join(lst) #from lst to string
                    i+=1
            if i==n-1:
                ans.append(ele)
        return ans
