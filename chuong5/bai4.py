import os

thu_muc_hien_tai = os.path.dirname(__file__)
ten_file = os.path.join(thu_muc_hien_tai, 'setInfo.txt')

# Nhập thông tin từ bàn phím
print("Vui lòng nhập thông tin cá nhân:")
ten = input("Tên: ")
tuoi = input("Tuổi: ")
email = input("Email: ")
skype = input("Skype: ")
dia_chi = input("Địa chỉ: ")
noi_lam_viec = input("Nơi làm việc: ")

# Gom thông tin lại
thong_tin = f"Tên: {ten}\nTuổi: {tuoi}\nEmail: {email}\nSkype: {skype}\nĐịa chỉ: {dia_chi}\nNơi làm việc: {noi_lam_viec}\n"

# a) Lưu các thông tin trên vào file 'setInfo.txt'
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(thong_tin)
print("\nĐã lưu thông tin vào file thành công!\n")

# b) Đọc thông tin từ file 'setInfo.txt' và hiển thị kết quả ra màn hình
print("--- Kết quả đọc từ file ---")
with open(ten_file, 'r', encoding='utf-8') as file:
    print(file.read())