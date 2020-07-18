# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
class Solution:
    def invalidTransactions(self, transactions):
        #transactions: List[str]) -> List[str]:
        store=collections.defaultdict(list)
        for trans in transactions:
            name,time,amount,city = trans.split(",")
            #转换格式 方便排序
            store[name].append([name,int(time),int(amount),city])
        def convert(l): 
            return l[0]+","+str(l[1])+","+str(l[2])+","+l[3]
            #再转换回原始数据，方便输出
        res=set()
        for name,value in store.items():
            transaction=sorted(value,key=lambda x:x[1])
            for i in range(len(transaction)):
                if transaction[i][2]>1000:
                    res.add(convert(transaction[i]))
                for j in range(i+1,len(transaction)):                    
                    if abs(transaction[j][1]-transaction[i][1])>60:
                        break
                    if transaction[j][3]!=transaction[i][3]:
                        res.add(convert(transaction[i]))
                        res.add(convert(transaction[j]))
        return res
        