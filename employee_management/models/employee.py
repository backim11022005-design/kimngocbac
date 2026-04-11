from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, age, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.base_salary = base_salary
        self.performance_score = 0
        self.projects = []

    @abstractmethod
    def calculate_salary(self): pass

    def update_performance(self, score):
        if not (0 <= score <= 10):
            raise ValueError("Điểm hiệu suất phải từ 0-10")
        self.performance_score = score

    def __str__(self):
        role = type(self).__name__
        return f"[{self.emp_id}] {self.name:15} | {role:10} | Lương: {self.calculate_salary():,.0f} | Dự án: {len(self.projects)}"