# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:38:46 2020

@author: Di Wang
"""

class Solution:
    def maxDistToClosest(self, seats):
        seat=[]
        for i in range(len(seats)):
            if seats[i]==1:
                seat.append(i)
        if len(seat)==1:
            return max(seat[0],len(seats)-seat[0]-1)
        distance=0
        for j in range(len(seat)-1):
            distance=max((seat[j+1]-seat[j])//2,distance)
        distance=max(distance,seat[0],len(seats)-seat[-1]-1)
        return distance