# https://edabit.com/challenge/pa65DgwG5HMbtf6iY
# Meduim
# 07.09.2024

# But in this challenge Python (3.4)
# in this version we don't have formating


class player():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f'{self.name} is age {self.age}'

    def get_height(self):
        return f'{self.name} is {self.height}cm'

    def get_weight(self):
        return f'{self.name} weighs {self.weight}kg'
