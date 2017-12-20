# -*- coding: utf-8 -*-
# e7_3.py

"promos列表中的值使用promotion装饰器填充"

proms = []

def promotion(prom_func):
	proms.append(prom_func)

@promotion
def fidelity(order):

	return order.total() * 0.05 if order.custmor.fidelity >= 1000 else 0

@promotion
def but_item(order):
	"单个商品为20以及以上提供10%折扣"
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount == item.total * 0.1
	return discount

@promotion
def large_order(order):
	"""订单中的不同商品达到10个或以上时提供7%折扣"""
	distinct_items = {item.product for item in order.cart}
	if len(distinct_items) >= 10:
		return order.total() * .07
	return 0

def best_promo(order):
	"""选择可用的最佳折扣	"""

	return max(promo(order) for promo in promos)