# -*- coding: utf-8 -*-

symbols = '$#%'
codes = [ord(symbol) for symbol in symbols if int(ord(symbol)) > 35]

print(codes)