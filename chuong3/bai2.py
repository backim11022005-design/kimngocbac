n = int(input("Nhập n: "))
if n > 10:
    print("Số nhập vào phải bé hơn 10.")
else:
    print(f"Các số chẵn từ 1 đến {n} là:")
    for i in range(2, n + 1, 2):
        print(i, end=" ")