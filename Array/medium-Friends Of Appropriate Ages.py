# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections #count the ages into a dictionary
class Solution:
    def numFriendRequests(self, ages):
        #ages: List[int]) -> int:
        count=collections.Counter(ages)
        ages.sort()
        res=0
        for A in list(set(ages)):
            for B in range(A//2+7+1,A+1):
                res+=count[A]*(count[B]-int(A==B))
        return res
