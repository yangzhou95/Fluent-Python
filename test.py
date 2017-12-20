# -*- coding :utf-8 -*-
from numpy import *
s = array([2, 1, 2, 2, 1, 2, 2, 2, 2, 3, 2, 3])
b = array([83, 84, 88, 90, 86, 78, 85, 87, 85, 84, 85, 77])
sum1 = sum(s*b.T) / sum(s)

print(sum1)