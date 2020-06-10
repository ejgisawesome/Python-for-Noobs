# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:16:13 2020

@author: egarcia
"""


## CALCULATOR PROGRAM

# will be better

import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

## exponents are ** btw

previous = 0
run = True

def performMath():
    
    global run
    global previous #so it can find it
    equation = ""
    if previous == 0:
        equation = input("Enter equation.")
    else:
        equation = input(str(previous))
        
        
        
        
    if equation == 'quit':
        run = False
        print("Smell ya later!")
    else:
        equation = re.sub('[A-Za-z,.:()" "]',"",equation)
       
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print(previous)

while run:
    performMath()
    
# use built in function called eval
    
# eval function can wreck (don't use on Hello World)
    
    ## what's RedJacket?
    