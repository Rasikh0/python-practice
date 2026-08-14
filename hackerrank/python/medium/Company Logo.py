#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    s = sorted(s)
    
    frequency = {}
    
    for letter in s:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    
    frequency_sorted = sorted(frequency.items(), key=lambda x:(-x[1], x[0]))
    for k, v in frequency_sorted[:3]:
        print(k, v)
