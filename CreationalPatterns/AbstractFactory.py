# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:17:34 2023

@author: shiva
"""

from abc import ABC, abstractmethod

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass
    
class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()
    

class SquareFactory(ShapeFactory):
    def create_shape(self):
        return Square()
    

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    

class Circle(Shape):
    def draw(self):
        return "Drawing Circle"


class Square(Shape):
    def draw(self):
        return "Drawing Square"
    

factory = CircleFactory()
shape = factory.create_shape()
print(shape.draw())