class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def getSalary(self):
        return self.salary

udit = Employee("udit", 95)
print(udit.salary)
print(udit.name)
