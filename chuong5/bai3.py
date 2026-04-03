import os

thu_muc_hien_tai = os.path.dirname(__file__)
ten_file = os.path.join(thu_muc_hien_tai, 'demo_file1.txt')
noi_dung = 'Thuc \n hanh \n voi \n file\n IO\n'

# Tạo file và ghi nội dung
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(noi_dung)

# a) In ra màn hình nội dung file đó trên một dòng
print("a) In ra màn hình nội dung file đó trên một dòng:")
with open(ten_file, 'r', encoding='utf-8') as file:
    # Đọc toàn bộ và thay thế ký tự xuống dòng '\n' bằng khoảng trắng
    noi_dung_mot_dong = file.read().replace('\n', ' ')
    print(noi_dung_mot_dong)

print("\n" + "-"*40 + "\n")

# b) In ra màn hình nội dung file đó theo từng dòng
print("b) In ra màn hình nội dung file đó theo từng dòng:")
with open(ten_file, 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='') # end='' để không in dư khoảng trắng xuống dòng