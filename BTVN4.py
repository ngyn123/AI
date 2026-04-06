from pathlib import Path
from typing import List

def ghi_file_van_ban(duong_dan: str, noi_dung: List[str]) -> bool:
    """Ghi danh sách chuỗi vào file text. Trả về True nếu thành công."""
    file_path = Path(duong_dan)
    try:
        # 'w' là chế độ ghi đè (write). Dùng 'a' (append) nếu muốn ghi nối thêm.
        with file_path.open(mode='w', encoding='utf-8') as file:
            for dong in noi_dung:
                file.write(f"{dong}\n")
        return True
    except PermissionError:
        print(f"Lỗi: Không có quyền ghi vào file '{duong_dan}'.")
        return False
    except Exception as e:
        print(f"Lỗi hệ thống khi ghi file: {e}")
        return False

def doc_file_van_ban(duong_dan: str) -> List[str]:
    """Đọc file text và trả về danh sách các dòng (đã xóa ký tự xuống dòng)."""
    file_path = Path(duong_dan)
    # Kiểm tra file có tồn tại trước khi đọc
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file tại: {duong_dan}")
        
    try:
        # 'r' là chế độ đọc (read). Context Manager tự động đóng file sau khi thoát khối lệnh
        with file_path.open(mode='r', encoding='utf-8') as file:
            # Dùng list comprehension để cắt bỏ ký tự \n ở cuối mỗi dòng
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Lỗi hệ thống khi đọc file: {e}")
        return []

# --- Khối kiểm thử ---
if __name__ == "__main__":
    file_name = "du_lieu_demo.txt"
    du_lieu_dau_vao = ["Dòng 1: Hệ thống khởi động", "Dòng 2: Dữ liệu an toàn", "Dòng 3: Kết thúc"]
    
    # Thực thi Ghi
    if ghi_file_van_ban(file_name, du_lieu_dau_vao):
        print(f"Đã ghi thành công vào {file_name}")
        
    # Thực thi Đọc
    try:
        du_lieu_doc_duoc = doc_file_van_ban(file_name)
        print("\nNội dung đọc được từ file:")
        for index, dong in enumerate(du_lieu_doc_duoc, start=1):
            print(f"{index} | {dong}")
    except FileNotFoundError as error:
        print(error)