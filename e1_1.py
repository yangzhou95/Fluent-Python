# -*- coding: utf-8 -*-

import collections

# 构建一个简单的类来表示一张纸牌
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades dimonds clubs hearts'.split() 

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits 
										for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	# 定义__getitem__,可进行索引操作；
	def __getitem__(self, position):
		return self._cards[position]

	def spades_high(card):
		rank_value = FrenchDeck.ranks.index(card.rank)
		return rnk_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
	deck = FrenchDeck()
	l = len(deck)
	print(l)
	deck[0]
	# for card in deck:
	# 	print(card)