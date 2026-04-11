def format_employee_table(employees):
    header = f"{'ID':<10} | {'Họ Tên':<20} | {'Chức Vụ':<12} | {'Lương':>15}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for e in employees:
        role = type(e).__name__
        salary = f"{e.calculate_salary():,.0f}"
        print(f"{e.emp_id:<10} | {e.name:<20} | {role:<12} | {salary:>15}")
    print("-" * len(header))