# -*- coding: utf-8 -*-
# calls.py

class Callee():
	def __call__(self, x=9, *pargs, **kargs):
		print('Called: ',x,  pargs, kargs)


C = Callee()
print(C(1,2,3))
print(C(1,2,3,m=4,n=5))
