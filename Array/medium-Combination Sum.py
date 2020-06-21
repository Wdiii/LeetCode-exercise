# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def combinationSum(self, candidates, target):
        #candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        candidates.sort()
        self.getTarget(candidates, target, 0, [])
        return self.res
    def getTarget(self,candidates,target,start,temlist):
        if target==0:
            return self.res.append(temlist)
        for i in range(start,len(candidates)):
            if target<candidates[i]:
                break
            else:
                self.getTarget(candidates,target-candidates[i],i,temlist+[candidates[i]])
        