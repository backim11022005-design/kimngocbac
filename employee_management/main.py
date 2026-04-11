import random
from models import Manager, Developer, Intern
from services.company import Company
from services.payroll import PayrollService
from exceptions.employee_exceptions import EmployeeException
from utils.validators import validate_age, validate_salary

def seed_data(company):
    """Nạp 10 nhân viên mẫu với tham số chuẩn xác"""
    names = ["An", "Bình", "Chi", "Dũng", "Em", "Phúc", "Giang", "Hương", "Khanh", "Linh"]
    langs = ["Python", "Java", "C++", "JavaScript"]
    unis = ["Bách Khoa", "Công Nghệ", "Kinh Tế"]
    
    for i in range(1, 11):
        eid = f"NV{i:02d}"
        age, sal = random.randint(22, 45), random.randint(10, 30)*1000000
        role_choice = random.choice(['mgr', 'dev', 'int'])
        
        # Sửa lỗi TypeError: Truyền đúng tham số riêng cho từng loại
        if role_choice == 'mgr':
            emp = Manager(eid, names[i-1], age, sal, team_size=random.randint(5, 15))
        elif role_choice == 'dev':
            emp = Developer(eid, names[i-1], age, sal, language=random.choice(langs))
        else:
            emp = Intern(eid, names[i-1], age, sal, university=random.choice(unis))
            
        emp.update_performance(random.randint(3, 10))
        # Gán dự án ngẫu nhiên để test chức năng thống kê
        for _ in range(random.randint(1, 4)):
            emp.projects.append(f"Project_{random.randint(1, 5)}")
        company.add_employee(emp)

def main():
    my_company = Company("ABC Corp")
    seed_data(my_company)
    
    while True:
        # Khôi phục đầy đủ giao diện Menu từ hình ảnh yêu cầu
        print("\n" + "="*45)
        print(f"{'HỆ THỐNG QUẢN LÝ NHÂN VIÊN ABC':^45}")
        print("="*45)
        print("1. Thêm nhân viên mới      5. Quản lý dự án")
        print("2. Hiển thị danh sách      6. Đánh giá hiệu suất")
        print("3. Tìm kiếm nhân viên      7. Quản lý nhân sự")
        print("4. Quản lý lương           8. Thống kê báo cáo")
        print("9. Thoát")
        
        choice = input("\nChọn chức năng (1-9): ")
        
        try:
            if choice == '1': # THÊM NHÂN VIÊN
                print("a. Thêm Manager | b. Thêm Developer | c. Thêm Intern")
                sub = input("Chọn loại: ").lower()
                eid, name = input("ID: "), input("Tên: ")
                age = validate_age(int(input("Tuổi: "))) # Xử lý Exception tuổi
                sal = validate_salary(float(input("Lương cơ bản: "))) # Xử lý Exception lương
                
                if sub == 'a': my_company.add_employee(Manager(eid, name, age, sal, 5))
                elif sub == 'b': my_company.add_employee(Developer(eid, name, age, sal, "Python"))
                else: my_company.add_employee(Intern(eid, name, age, sal, "FPT"))
                print(">>> Đã thêm thành công.")

            elif choice == '2': # HIỂN THỊ
                print("a. Tất cả | c. Theo hiệu suất (Cao -> Thấp)")
                sub = input("Chọn: ").lower()
                emps = list(my_company.employees.values())
                if not emps: raise IndexError("Chưa có dữ liệu") # Xử lý Exception rỗng
                if sub == 'c': emps.sort(key=lambda x: x.performance_score, reverse=True)
                for e in emps: print(e)

            elif choice == '4': # QUẢN LÝ LƯƠNG
                print("b. Tính tổng lương công ty | c. Top 3 nhân viên lương cao nhất")
                sub = input("Chọn: ").lower()
                emps = list(my_company.employees.values())
                if sub == 'b':
                    total = PayrollService.calculate_total_salary(emps)
                    print(f"Tổng quỹ lương: {total:,.0f} VNĐ")
                elif sub == 'c':
                    top3 = sorted(emps, key=lambda x: x.calculate_salary(), reverse=True)[:3]
                    for e in top3: print(f"{e.name}: {e.calculate_salary():,.0f} VNĐ")

            elif choice == '5': # QUẢN LÝ DỰ ÁN (Nâng cao)
                print("d. Top 10 nhiều dự án nhất | f. Danh sách NV tham gia 1 dự án")
                sub = input("Chọn: ").lower()
                if sub == 'd':
                    for e in sorted(my_company.employees.values(), key=lambda x: len(x.projects), reverse=True)[:10]:
                        print(f"{e.name}: {len(e.projects)} dự án")
                elif sub == 'f':
                    for e in [x for x in my_company.employees.values() if len(x.projects) == 1]:
                        print(f"[{type(e).__name__}] {e.name}")

            elif choice == '7': # QUẢN LÝ NHÂN SỰ
                print("a. Xóa nhân viên (nghỉ việc) | d. Cắt giảm nhân sự hàng loạt")
                sub = input("Chọn: ").lower()
                if sub == 'a':
                    eid = input("Nhập ID cần xóa: ")
                    my_company.remove_employee(eid) # Sẽ báo lỗi nếu không tồn tại
                elif sub == 'd':
                    ids = input("Nhập các ID cách nhau bằng dấu phẩy: ").split(",")
                    removed = [my_company.employees.pop(i.strip()).name for i in ids if i.strip() in my_company.employees]
                    print(f">>> Đã cho nghỉ việc: {removed}")

            elif choice == '8': # THỐNG KÊ
                avg = PayrollService.get_average_projects(list(my_company.employees.values()))
                print(f"Số dự án trung bình: {avg:.2f}")

            elif choice == '9':
                print("Hệ thống đã đóng. Tạm biệt!"); break

        except Exception as e:
            print(f"(!) THÔNG BÁO: {e}")

if __name__ == "__main__":
    main()