import os

thu_muc_hien_tai = os.path.dirname(__file__)
ten_file = os.path.join(thu_muc_hien_tai, 'demo_file2.txt')

# Nội dung text (đã thêm 'dnu' để khớp với output mẫu)
noi_dung = 'Dem so luong tu xuat hien abc abc abc 12 12 it it dnu eaut'

# 1. Tạo file demo_file2.txt
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(noi_dung)

# 2. Đọc file và đếm số lượng từ
tu_dien_dem = {}
with open(ten_file, 'r', encoding='utf-8') as file:
    van_ban = file.read()
    danh_sach_tu = van_ban.split() # Cắt các từ ra dựa vào khoảng trắng
    
    for tu in danh_sach_tu:
        if tu in tu_dien_dem:
            tu_dien_dem[tu] += 1
        else:
            tu_dien_dem[tu] = 1

# 3. In kết quả trả về
print("Kết quả trả về:")
print(tu_dien_dem)