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

