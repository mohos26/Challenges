# https://edabit.com/challenge/6Ran7nuFijxkXD95o
# 31.1.2023

def keyboard_shortcut(txt):
    v = ''
    for i in range(txt.count('Ctrl + C') + txt.count('Ctrl + V')):
        t1, t2 = '', ' '
        if -1 < txt[0:].find('Ctrl + C') < txt[0:].find('Ctrl + V'):
            v = txt[:txt[0:].find('Ctrl + C')].rstrip()
            if txt[:txt[0:].find('Ctrl + C')].strip() != '' and txt[txt[0:].find('Ctrl + C')+9:] != '':
                t1 = ' '
            txt = txt[:txt[0:].find('Ctrl + C')].rstrip() + t1 + txt[txt[0:].find('Ctrl + C')+9:]
        else:
            if txt[txt[0:].find('Ctrl + V') + 9:] == '' or txt[:txt[0:].find('Ctrl + V')] == '':
                t2 = ''
            txt = txt[:txt[0:].find('Ctrl + V')] + v + t2 + txt[txt[0:].find('Ctrl + V') + 9:]
    return txt


def keyboard_shortcut2(txt):
	aid = ""
	while True:
		aid2 = txt.find("Ctrl + C")
		aid3 = txt.find("Ctrl + V")
		loop = 0
		if aid2 == -1 and aid3 == -1:
			break
		elif aid2 == -1 or aid3 < aid2:
			lst = []
			lst2 = [txt[:aid3].strip(), aid.strip(), txt[aid3+8:].strip()]
			for i in range(3):
				if lst2[i]:
					lst.append(lst2[i])
			txt = ' '.join(lst).strip()
		elif aid3 == -1 or aid2 < aid3:
			aid = txt[:aid2].strip()
			txt = ' '.join([txt[:aid2].strip(), txt[aid2+8:].strip()]).strip()
			# print("->", txt)
	return txt


print(keyboard_shortcut2("You gotta paste at Ctrl + C some point my Ctrl + C guy"))
