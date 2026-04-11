from .employee import Employee
class Manager(Employee):
    def __init__(self, emp_id, name, age, base_salary, team_size):
        super().__init__(emp_id, name, age, base_salary)
        self.team_size = team_size
    def calculate_salary(self): return self.base_salary + 5000000