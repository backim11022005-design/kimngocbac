_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
n_min = 4
dem = 0
for s in _list:
    if len(s) >= n_min and s[0] == s[-1]:
        dem += 1
print("Kết quả:", dem)