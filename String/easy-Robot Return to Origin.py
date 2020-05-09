# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R")
