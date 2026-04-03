import os
import ast
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import docx2txt

def compare_python_files(file1, file2):
    """Đánh giá trùng lặp code Python (Text và Logic)"""
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        code1 = f1.read()
        code2 = f2.read()

    # 1. So sánh Text (bề mặt)
    seq = difflib.SequenceMatcher(None, code1, code2)
    text_sim = seq.ratio() * 100

    # 2. So sánh Logic (Cây cú pháp AST)
    try:
        ast1 = ast.dump(ast.parse(code1))
        ast2 = ast.dump(ast.parse(code2))
        seq_ast = difflib.SequenceMatcher(None, ast1, ast2)
        logic_sim = seq_ast.ratio() * 100
    except SyntaxError:
        logic_sim = 0.0 # Nếu file code bị lỗi cú pháp

    return text_sim, logic_sim

def extract_text_from_docx(file_path):
    """Trích xuất văn bản từ file Word"""
    try:
        return docx2txt.process(file_path)
    except Exception:
        return ""

def compare_reports(file1, file2):
    """Đánh giá trùng lặp báo cáo (Dùng TF-IDF và Cosine Similarity)"""
    text1 = extract_text_from_docx(file1)
    text2 = extract_text_from_docx(file2)
    
    if not text1 or not text2:
        return 0.0
        
    documents = [text1, text2]
    tfidf_vectorizer = TfidfVectorizer(stop_words=None)
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0] * 100

def get_all_files(folder_path, extension):
    """Lấy danh sách tất cả các file có đuôi mở rộng cụ thể trong thư mục"""
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

# ==========================================
# HÀM CHÍNH (MAIN) 
# ==========================================
if __name__ == "__main__":
    print("--- CÔNG CỤ ĐÁNH GIÁ TRÙNG LẶP SẢN PHẨM ---")
    
    # Chỉ định 2 thư mục lớn chứa sản phẩm
    thu_muc_SP1 = "thu_muc_A"
    thu_muc_SP2 = "thu_muc_B"

    # Lấy danh sách toàn bộ file cần quét
    py_files_1 = get_all_files(thu_muc_SP1, ".py")
    py_files_2 = get_all_files(thu_muc_SP2, ".py")
    docx_files_1 = get_all_files(thu_muc_SP1, ".docx")
    docx_files_2 = get_all_files(thu_muc_SP2, ".docx")

    # 1. ĐÁNH GIÁ TRÙNG LẶP CODE
    print("\n[1] KẾT QUẢ ĐÁNH GIÁ MÃ NGUỒN:")
    if not py_files_1 or not py_files_2:
        print("Không tìm thấy đủ file .py trong 2 thư mục để so sánh.")
    else:
        for file1 in py_files_1:
            for file2 in py_files_2:
                text_sim, logic_sim = compare_python_files(file1, file2)
                print(f"- So sánh: '{os.path.basename(file1)}' & '{os.path.basename(file2)}'")
                print(f"  + Trùng lặp Text: {text_sim:.2f}%")
                print(f"  + Trùng lặp Logic: {logic_sim:.2f}%")

    # 2. ĐÁNH GIÁ TRÙNG LẶP BÁO CÁO
    print("\n[2] KẾT QUẢ ĐÁNH GIÁ BÁO CÁO:")
    if not docx_files_1 or not docx_files_2:
         print("Không tìm thấy đủ file .docx trong 2 thư mục để so sánh.")
    else:
        for doc1 in docx_files_1:
            for doc2 in docx_files_2:
                report_sim = compare_reports(doc1, doc2)
                print(f"- So sánh: '{os.path.basename(doc1)}' & '{os.path.basename(doc2)}'")
                print(f"  + Mức độ giống nhau: {report_sim:.2f}%")