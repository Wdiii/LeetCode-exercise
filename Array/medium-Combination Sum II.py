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
        self.getTarget(candidates,target,0,[])
        return self.res
    def getTarget(self,candidates,target,i,temList):
        if target==0 and temList not in self.res:
            return self.res.append(temList)
        for i in range(i,len(candidates)):
            if target<candidates[i]:
                break
            else:
                self.getTarget(candidates,target-candidates[i],i+1,temList+[candidates[i]])
    