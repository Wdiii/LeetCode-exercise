# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def numRabbits(self, answers):
        #answers: List[int]) -> int:
        if len(answers)==0:
            return 0
        dic={}
        for i in answers:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        count=0
        for k,v in dic.items():
            if k==0 or v%(k+1)==0:
                count+=v
            else:
                count+=(int(v/(k+1))+1)*(k+1)
        return count