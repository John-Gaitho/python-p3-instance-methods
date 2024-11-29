#!/usr/bin/env python3

class Dog:
    # Class body goes here
     def __init__(self, name):
        self.name = name
    #Instance method definition
     def bark(self):
        return f"{self.name} says Woof! "