# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def distributeCandies(self, candies, num_people):
        #candies: int, num_people: int) -> List[int]:
        a,b=1,0
        lst=[0]*num_people
        while candies>0:
            lst[b]+=min(a,candies)
            candies-=a
            a+=1
            if b!=num_people-1:
                b+=1
            else:
                b=0
        return lst


#faster solution by leetcode
class Solution1:
    def distributeCandies(self, candies, n):
        ans=[0]*n
        i=0
        last=1
        while candies :
            if last>=candies :
                ans[i]+=candies
                break
            ans[i]+=last
            candies-=last
            last=last+1
            i+=1
            if i==n :
                i=i%n
        return ans