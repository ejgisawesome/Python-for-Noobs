# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:52:47 2020

@author: egarcia
"""


run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1

# += add to counter

## printed 1 to 99