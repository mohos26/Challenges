# https://edabit.com/challenge/Rep3fHbrLGKDatZ2L
# Expect
# 22.09.2024

from math import ceil

def _pattern(pat, lenght, ind=None):
	res = ''
	res += pat*(lenght//len(pat))
	res += pat[:lenght%len(pat)]
	if ind is not None:
		return res[:ind] + '_' + res[ind+1:]
	return res

def complete_pattern(txt):
	aid = txt.index('_')
	if aid < ceil(len(txt)/2)-len(txt)%2:
		main = txt[aid+1:]
	else:
		main = txt[:aid]
	i = 0
	while i < len(main)//2:
		if main[:i+1]*(len(main)//(i+1)) in main:
			if _pattern(main[:i+1], len(txt), aid) == txt:
				return _pattern(main[:i+1], len(txt))[aid]
			i = -1
			main = main[1:]
		i += 1
	i = ceil(len(main)/2)
	while i < len(main):
		if main[i:] in main[:i]:
			if _pattern(main[:i], len(txt), aid) == txt:
				return _pattern(main[:i], len(txt))[aid]
			i = -1
			main = main[1:]
		i += 1
	return _pattern(main, len(txt))[aid]

# 17.08.2025

def split_chunks(s, i):
	j = 0
	res = []
	while j < len(s):
		res.append(s[j:j+i])
		j += i
	return res

def extract_base_missing(lst):
	base, missing = "", ""
	for arg in lst:
		if base and missing:
			break
		if '_' in arg:
			missing = arg
		elif not base:
			base = arg
	return base, missing

def validate_chunks(lst, base):
	for arg in lst:
		for i, letter in enumerate(arg):
			if letter == '_':
				continue
			elif letter != base[i]:
				return False
	return True

def complete_pattern(s):
	for i in range(1, len(s)):
		lst = split_chunks(s, i)
		base, missing = extract_base_missing(lst)
		if validate_chunks(lst, base):
			return base[missing.index('_')]
	return None
