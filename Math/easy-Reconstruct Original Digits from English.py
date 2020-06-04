# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def originalDigits(self, s: str) -> str:
        dic={"o":0,"n":0,"e":0,"t":0,"w":0,"h":0,"r":0,"f":0,"u":0,"i":0,"v":0,"s":0,"x":0,
            "n":0,"g":0,"z":0}
        for i in range(len(s)):
            if dic[s[i]]==0:
                dic[s[i]]=1
            else:
                dic[s[i]]+=1
        a,b,c,d,e=0,0,0,0,0
        if dic["z"]!=0:
            a=dic["z"]
            dic["e"]-=a
            dic["r"]-=a
            dic["o"]-=a
        if dic["w"]!=0:
            b=dic["w"]
            dic["t"]-=b
            dic["o"]-=b
        if dic["u"]!=0:
            c=dic["u"]
            dic["f"]-=c
            dic["o"]-=c
            dic["r"]-=c
        if dic["x"]!=0:
            d=dic["x"]
            dic["s"]-=d
            dic["i"]-=d
        if dic["g"]!=0:
            e=dic["g"]
            dic["e"]-=e
            dic["i"]-=e
            dic["h"]-=e
            dic["t"]-=e
        res="0"*a+"1"*dic["o"]+"2"*b+"3"*dic["t"]+"4"*c+"5"*dic["f"]+"6"*d+"7"*dic["s"]+"8"*e+"9"*(dic["i"]-dic["f"])
        return res
            
        