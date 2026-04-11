from exceptions.employee_exceptions import *

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def add_employee(self, employee):
        if employee.emp_id in self.employees:
            employee.emp_id = f"{employee.emp_id}_new" # Tự động sinh ID mới
        self.employees[employee.emp_id] = employee

    def get_top_10_projects(self, most=True):
        """Thống kê Top 10 dự án"""
        emps = list(self.employees.values())
        return sorted(emps, key=lambda x: len(x.projects), reverse=most)[:10]

    def layoff_bulk(self, ids):
        """Cắt giảm nhân sự hàng loạt"""
        return [self.employees.pop(eid).name for eid in ids if eid in self.employees]