#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:55:27 2019

@author: kwenzakonkemncwango
"""

#import sys

#sys.path

def fizzbuzz(number):
    if number % 3 == 0:
        return "FIZZ"
    elif number % 5 == 0:
        return "BUZZ"
    else:
        return number