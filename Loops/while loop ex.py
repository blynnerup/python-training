# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:52:23 2023

@author: BrianLynnerupPederse
"""

num = 1

print("While loop")

while num < 11:
    smiley = "\U0001f600" * num
    print(smiley)
    num += 1
    
print("For loop")
num = 11
for i in range(1, num):
    smiley = "\U0001f600" * i
    print(smiley)