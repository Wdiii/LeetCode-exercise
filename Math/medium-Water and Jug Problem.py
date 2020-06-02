# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)        
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)

#倒水问题，转换为两个杯子向一个大杯子中倒水、舀水的问题，
#即mx+ny=d,若z<=x+y且z%d==0,说明存在m、n使得最终剩余水为z。
#根据贝祖等式，d为x、y的最大公约数