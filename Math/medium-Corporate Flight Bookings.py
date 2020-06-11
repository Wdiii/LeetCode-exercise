# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def corpFlightBookings(self, bookings, n):
        #bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n
        for i in range(len(bookings)):
            while bookings[i][0]<=bookings[i][1]:
                res[bookings[i][0]-1]+=bookings[i][2]
                bookings[i][0]+=1
        return res
            
#Time Limit Exceeded

class Solution1:
    def corpFlightBookings(self, bookings, n):
        res=[0]*(n+1)
        for i,j,k in bookings:
            res[i-1]+=k
            res[j]-= k
        for i in range(1,n+1):
            res[i]+=res[i-1]
        return res[:-1]
        