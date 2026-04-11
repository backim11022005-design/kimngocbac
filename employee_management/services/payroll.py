class PayrollService:
    @staticmethod
    def calculate_total_salary(employees):
        return sum(e.calculate_salary() for e in employees)

    @staticmethod
    def get_average_projects(employees):
        if not employees:
            return 0
        total_p = sum(len(e.projects) for e in employees)
        return total_p / len(employees)