# -*- coding : utf-8 -*-

class TwilightBus():

	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)
			# list创建 passengers 列表的副本；如果不是列表，就把它转换成列表
	def pick(self, name):
		self.passengers.append(name)

	def drop(self, name):
		self.passengers.remove(name)

if __name__ == '__main__':
	basketball_team = ['Sue', 'Tina', 'Mary', 'Tony']
	bus = TwilightBus(basketball_team)
	bus.drop('Tony')
	bus.drop('Sue')
	print(basketball_team)

