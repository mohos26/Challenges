# https://edabit.com/challenge/S7rdJsn6vkfC9BzcR
# Hard
# 11.09.2024


class Employee:
    def __init__(self, fullname, salary=0, height=0, nationality='', subordinates=[]):
        self.name, self.lastname = fullname.split()
        if salary:
            self.salary = salary
        if height:
            self.height = height
        if nationality:
            self.nationality = nationality
        if subordinates:
            self.subordinates = subordinates

