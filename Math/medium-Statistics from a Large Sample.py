# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def sampleStats(self, count):
        #count: List[int]) -> List[float]:
        for i in range(len(count)):
            if count[i]!=0:
                minpoint=i
                break
        for j in range(len(count)-1,-1,-1):
            if count[j]!=0:
                maxpoint=j
                break
        total,number=0,0
        numbers=sum(count)
        flag=True
        for m in range(i,j+1):
            if count[m]!=0:
                total+=count[m]*m
                number+=count[m]
                if flag==True and number>numbers/2:
                    if numbers%2!=0:
                        median=m
                    else:
                        if number-count[m]<numbers/2:
                            median=m
                        else:
                            median=(m+m-1)/2
                    flag=False            
        mean=total/numbers
        mode=count.index(max(count))
        return [minpoint, maxpoint, mean, median, mode]
        