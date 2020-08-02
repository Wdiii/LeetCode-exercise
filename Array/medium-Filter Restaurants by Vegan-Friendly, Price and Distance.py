# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        #restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if not restaurants:
            return []
        res=[]
        for i,r,v,p,d in restaurants:
            if not veganFriendly or (v and veganFriendly):
                if p<=maxPrice and d<=maxDistance:
                    res.append ([i,r])
        return [i for i,r in sorted(res, key=lambda x:(x[1],x[0]), reverse=True)]
    