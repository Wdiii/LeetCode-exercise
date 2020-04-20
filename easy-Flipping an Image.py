# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Solution:
    def flipAndInvertImage(self, A):
        for c, list in enumerate(A):
            A[c] = [1 if j == 0 else 0 for j in list]
            A[c].reverse()
        return A
