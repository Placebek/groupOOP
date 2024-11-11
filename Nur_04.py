class Employee:
    def _init_(self, name, position): 
        self.info = f"{name}, {position}"

class Company:
    def _init_(self): 
        self.employees = []

    def hire(self, employee): 
        self.employees.append(employee)

    def fire(self, employee): 
        self.employees.remove(employee)

    def show_employees(self): 
        for emp in self.employees: print(emp.info)


# Мысал
company = Company()
emp1, emp2 = Employee("John", "Dev"), Employee("Jane", "HR")
company.hire(emp1)
company.hire(emp2)
company.show_employees()

company.fire(emp1)
company.show_employees()