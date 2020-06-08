# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
class Solution:
    def primePalindrome(self, N: int) -> int:
        if N==1:
            return 2
        elif N in [2, 3, 5, 7, 11]:
            return N
        while N < 2*10**8:
            if self.is_palindrome(N) and self.is_prime(N):
                return N
                break
            else:
                if N%2==0:
                    N+=1
                else:
                    N+=2 
        
    def is_palindrome(self,N):
        n=list(str(N))
        return n==n[::-1]
    
    def is_prime(self,N):
        flag=False
        if N%2==0:
            return flag
        for i in range(3,int(math.sqrt(N))+1):
            if i%2!=0:
                if N%i==0:
                    flag=False
                    break
                else:
                    flag=True
        return flag

#Time Limit Exceeded,find a way to improve it from online resource

class Solution1:
    def primePalindrome(self, N):
        while True:
            if N in [2, 3, 5, 7, 11]:
                return N
            elif N == 1:
                return 2
 #若N的位数是偶数时，那么除了11其他的都不是素数,
 #如 1001的位数是4，那么接下来应该从10001开始，因为在1001-9999不会有素数的           
            if (N > 11) and (len(str(N)) % 2 == 0):
                N = int(pow(10, len(str(N)))) + 1
                continue
            if self.is_palindrome(N) and self.is_prime(N):
                return N
            
            if N % 2 != 0:
                N = N + 2
            else:
                N = N + 1
 
    def is_palindrome(self,N):
        n=list(str(N))
        return n==n[::-1]
    
    def is_prime(self,N):
        flag=False
        if N%2==0:
            return flag
        for i in range(3,int(math.sqrt(N))+1):
            if i%2!=0:
                if N%i==0:
                    flag=False
                    break
                else:
                    flag=True
        return flag
