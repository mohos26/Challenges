# https://edabit.com/challenge/gB7nt6WzZy8TymCah
# Meduim
# 10.09.2024


class Employee:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.fullname = fname + ' ' + lname
        self.email = fname.lower() + '.' + lname.lower() + '@company.com'

