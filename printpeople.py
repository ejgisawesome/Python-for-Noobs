# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:42:55 2020

@author: egarcia
"""


def print_people (*people):
    for person in people:
        print("This person is", person + ".")
    
print_people("Stan","Kyle","Eric","Kenny","Butters")
