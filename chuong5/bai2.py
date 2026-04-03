import os

# Tự động lấy đường dẫn thư mục chứa file code hiện tại (chuong5)
thu_muc_hien_tai = os.path.dirname(__file__)
ten_file = os.path.join(thu_muc_hien_tai, 'bai2.txt')

van_ban_mau = "Lão hạc."

# 1. Ghi đoạn văn bản vào tập tin
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(van_ban_mau)
print(f"Đã ghi thành công vào file '{ten_file}'.\n")

# 2. Đọc và hiển thị văn bản đó
print("--- Nội dung file vừa ghi ---")
with open(ten_file, 'r', encoding='utf-8') as file:
    print(file.read())