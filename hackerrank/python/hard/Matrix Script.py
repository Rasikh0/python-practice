#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
temp = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for j in range(m):
    for i in matrix:
        temp.append(i[j])
      
temp = "".join(temp)
t = re.sub(r"(?<=[A-Za-z0-9])[!,@,#,$,%,&,\s]+(?=[A-Za-z0-9])"," ", temp)
print(t)
