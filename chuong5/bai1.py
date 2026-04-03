def doc_n_dong_dau(ten_file):
    try:
        n = int(input("Nhập số dòng n cần đọc: "))
        with open(ten_file, 'r', encoding='utf-8') as file:
            print(f"\n--- {n} dòng đầu tiên của file ---")
            for i in range(n):
                line = file.readline()
                if not line: # Nếu file có ít hơn n dòng thì dừng
                    break
                print(line, end='')
            print() # In thêm một dòng trống cuối cùng cho dễ nhìn
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'! Vui lòng tạo file này trước.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

# GỌI HÀM: Dòng này sẽ kích hoạt chương trình chạy
doc_n_dong_dau('chuong5/test.txt')