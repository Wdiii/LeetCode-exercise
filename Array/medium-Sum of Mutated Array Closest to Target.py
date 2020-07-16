# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def findBestValue(self, arr, target):
        #arr: List[int], target: int) -> int:
        left,right=0,max(arr)
        diff,ans=float("inf"),float("inf")
        #float("inf"), float("-inf") 正负无穷
        while left<=right:
            mid=(left+right)//2
            temp=0
            for a in arr:
                if a<=mid:
                    temp+=a
                else:
                    temp+=mid
            cur_diff=abs(temp-target)
            if cur_diff<diff:
                diff=cur_diff
                ans=mid
            elif cur_diff==diff:
                ans=min(ans,mid)
            if temp>target:
                right=mid-1
            elif temp<target:
                left=mid+1
            elif temp==target:
                return mid
        return ans
                