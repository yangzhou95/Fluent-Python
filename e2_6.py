# -*- coding: utf-8 -*-

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in sizes for s in  colors):
	print(tshirt)