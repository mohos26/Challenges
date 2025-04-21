# https://edabit.com/challenge/kbtju9wk5pjGYMmHF
# Meduim
# 10.09.2024


class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = self.fname + ' ' + self.lname
        self.initials = self.fname[0] + '.' + self.lname[0]
