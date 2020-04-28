# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday")
        return days[datetime.date(year,month,day).weekday()]
    
#https://docs.python.org/3/library/datetime.html#module-datetime