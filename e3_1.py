# -*- coding: utf-8 -*- 
# e3_1.py
"""创建一个从一个单词到其出现情况的映射"""
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index.setdefault(word, []).append(location)
			# occurences = index.get(word, [])
			# occurences.append(location)
			# index[word] = occurences

# 以字母的顺序打印结果
for word in sorted(index, key = str.upper):
	print(word, index[word])