#
#
#

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)

    @classmethod
    def from_string(cls, s):
        firstname, lastname, salary = s.split('-')
        return cls(firstname, lastname, int(salary))


emp1 = Employee("Mary", "Sue", 60000)

emp2 = Employee.from_string("John-Smith-55000")

print(emp1.firstname)
print(emp2.firstname)
print(emp2.salary)
