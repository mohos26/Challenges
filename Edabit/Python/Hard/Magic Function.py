# https://edabit.com/challenge/sg7j2sT8yBbY7eFYG
# Hard
# 12.09.2024


class Magic:
    def replace(self, txt, s1, s2):
        for _ in range(txt.count(s1)):
            txt = txt[:txt.index(s1)] + s2 + txt[txt.index(s1)+1:]
        return txt # txt.replace(s1, s2)

    def str_length(self, txt):
        length = 0
        for _ in txt:
            length += 1
        return length # len(txt)

    def trim(self, txt):
        whitespace = ' \t\n\r\x0b\x0c'
        i, j = 0, self.str_length(txt)
        while txt[i] in whitespace:
            i += 1
        while txt[j-1] in whitespace:
            j -= 1
        return txt[i:j] # txt.strip()

    def list_slice(self, lst, limits):
        if limits[0] not in lst:
            return [limits[1]]
        aid1 = lst.index(limits[0])
        aid2 = lst.index(limits[1])
        return lst[aid1:aid2+1]

