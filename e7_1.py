# -*- coding: utf-8 -*- 
# e7_1.py

def deco(func):
	def inner():
		print('run inner()')
	return inner

@deco
def target():
	print('run target()')

# main
target()
