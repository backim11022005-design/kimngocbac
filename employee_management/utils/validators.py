import re
from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age):
    if not (18 <= age <= 65):
        raise InvalidAgeError(f"Tuổi {age} không hợp lệ (Phải từ 18-65)")
    return age

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lương phải là số dương")
    return salary

def validate_email(email):
    # Regex cơ bản kiểm tra định dạng email
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if not re.match(pattern, email):
        raise ValueError("Email sai định dạng (thiếu @ hoặc sai cấu trúc)")
    return email