# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        #words: List[str]) -> int:
        letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictionary = dict(zip(letter, code)) # 2 list to dictionary
        output=[]
        for ele in words:
            result=''
            for i in ele:
                result+=dictionary[i]
            if result not in output:
                output.append(result)
        return len(output)