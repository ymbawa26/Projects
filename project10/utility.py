""""
Yazan Bawaqna
CS152-B
December 4th 2022
This codes creats some utility functions for easier calculations
"""
import math
import setup

def height_percantage(percantage):
    """ this function calculates the number of pixels needed for a height of the required percentage"""
    return (setup.height/100) * percantage


def width_percantage(percantage):
    """ this function calculates the number of pixels needed for a width of the required percentage"""
    return (setup.width/100) * percantage
print(height_percantage(25))