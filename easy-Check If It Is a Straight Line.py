# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def checkStraightLine(self, coordinates):
        #coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        i=1
        result=True
        if coordinates[1][0]==coordinates[0][0]:
            while i < len(coordinates)-1:
                if coordinates[i+1][0] != coordinates[i][0]:
                    result = False
                    break
                else:
                    i+=1
        else:
            slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            while i < len(coordinates)-1:
                if coordinates[i+1][0] == coordinates[i][0]:
                    result = False
                    break
                elif(coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0]) != slope:
                    result=False
                    break
                else:
                    i+=1
        return result
