# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#Run out of time, need to improve
class Solution:
    def sumEvenAfterQueries(self, A, queries):
    #A: List[int], queries: List[List[int]]
        result=[]
        for i in range(len(queries)):
            A[queries[i][1]]=A[queries[i][1]]+queries[i][0]
            B=[]
            for ele in A:
                if ele%2==0:
                    B.append(ele)
            result.append(sum(B))
        return result

#After improvement
class Solution1:
    def sumEvenAfterQueries(self, A, queries):
        count=0
        for ele in A:
            if ele%2==0:
                count+=ele
        result=[]
        for i in range(len(queries)):
            if (A[queries[i][1]] % 2 ==0):
                if queries[i][0]%2==0:
                    count+=queries[i][0]
                else:
                    count-=A[queries[i][1]]
            else:
                if queries[i][0]%2!=0:
                    count+=queries[i][0]+A[queries[i][1]]
            A[queries[i][1]]=A[queries[i][1]]+queries[i][0]
            result.append(count)
        return result