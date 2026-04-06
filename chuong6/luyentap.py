# 1. Định nghĩa bảng mã (Từ điển)
cipher_dict = {
    'a': '!', 
    'b': '@', 
    'c': '#', 
    'd': '$',
    'e': '%',
    ' ': '_' # Mã hóa luôn cả dấu cách để bảo mật hơn
}

# 2. Hàm mã hóa
def encode_text(text, dictionary):
    encoded = ""
    for char in text.lower(): # Chuyển về chữ thường để khớp với từ điển
        # Nếu ký tự có trong từ điển thì lấy giá trị, nếu không thì giữ nguyên
        encoded += dictionary.get(char, char)
    return encoded

# 3. Hàm giải mã
def decode_text(encoded_text, dictionary):
    # Tạo từ điển ngược: {'!': 'a', '@': 'b', ...}
    reverse_dict = {v: k for k, v in dictionary.items()}
    
    decoded = ""
    for char in encoded_text:
        decoded += reverse_dict.get(char, char)
    return decoded

# --- CHƯƠNG TRÌNH CHÍNH ---
text_input = "bad cafe"

# Thực hiện mã hóa
encrypted = encode_text(text_input, cipher_dict)
print(f"Văn bản gốc: {text_input}")
print(f"Sau khi mã hóa: {encrypted}")

# Thực hiện giải mã
decrypted = decode_text(encrypted, cipher_dict)
print(f"Sau khi giải mã: {decrypted}")