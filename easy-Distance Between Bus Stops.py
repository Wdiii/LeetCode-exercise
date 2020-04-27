# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        #distance: List[int], start: int, destination: int) -> int:
        if start<destination:
            a=start
            b=destination
        else:
            a=destination
            b=start   
        clockwise=sum(distance[a:b])
        counterclockwise=sum(distance[:a])+sum(distance[b:])
        return min(clockwise,counterclockwise)
