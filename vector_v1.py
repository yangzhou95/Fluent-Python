# -*- coding: utf-8 -*-

from array import array
import reprlib
import math

class Vector:
	typecode = 'd'

	def __init__(self, components):
		# 受保护的实例属性self._components，将分量保存在一个数组中；
		self._components = array(self.typecode, components)

	def __iter__(self):
		# 构建一个迭代器
		return iter(self._components)

	def __repr__(self):
		# 使用 reprlib.repr() 函数获取 self._components的有限长度表示形式
		components = reprlib.repr(self._components)
		components = components[components.find('['):-1]
		return 'Vector({})'.format(components)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (byte([ord(self.typecode)]) + 
				byte(self._components))

	def __eq__(self, other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))

	def __bool__(self):
		return bool(abs(self))

	@classmethod
	def frombytes(cls, octets):
		typecode = chr(octets[0])
		memv = momryview(octets[1:]).cast(typecode)
		return cls(memv)