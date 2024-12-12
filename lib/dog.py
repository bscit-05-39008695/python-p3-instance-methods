#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

    #Instance method definition
    Dog = lambda self: print("Woof!")
    Dog = lambda self: print("The dog is sitting.")
