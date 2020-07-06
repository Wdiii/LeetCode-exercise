# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def leastInterval(self, tasks, n):
        #tasks: List[str], n: int) -> int:
        dic={}
        for i in tasks:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        top=max(dic.values())
        num_top=len([i for i,v in dic.items() if v==top])
        return max(num_top+(top-1)*(n+1),len(tasks))
    