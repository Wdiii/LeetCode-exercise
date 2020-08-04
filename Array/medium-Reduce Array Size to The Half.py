# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def minSetSize(self, arr):
        # arr: List[int]) -> int:
        n=(len(arr)+1)//2
        dict=collections.Counter(arr)
        lst=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        i=0
        total=lst[0][1]
        while total<n:
            i+=1
            total+=lst[i][1]
        return i+1
    