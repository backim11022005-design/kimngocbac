from .employee import Employee
class Intern(Employee):
    def __init__(self, emp_id, name, age, base_salary, university):
        super().__init__(emp_id, name, age, base_salary)
        self.university = university
    def calculate_salary(self): return self.base_salary * 0.8