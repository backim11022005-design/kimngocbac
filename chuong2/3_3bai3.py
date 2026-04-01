import time

x = time.localtime()
current_year = x[0]

birth_year = int(input("Nhập năm sinh của bạn: "))
age = current_year - birth_year

print(f"Năm sinh {birth_year}, vậy bạn {age} tuổi.")
