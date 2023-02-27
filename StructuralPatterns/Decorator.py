# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 08:33:00 2023

@author: shiva
"""

class RepeatDecorator():
    def __init__(self,num_repeats):
        self.num_repeats = num_repeats
        
    
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            for i in range(self.num_repeats):
                result = func(*args,**kwargs)
            return result
        return wrapper 
    


@RepeatDecorator(3)
def greet():
    print("Hello")

greet()

