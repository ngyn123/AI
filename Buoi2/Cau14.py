import random
import math
from typing import TypeAlias, Optional

Matrix: TypeAlias = list[list[int]]

def tao_mang_ngau_nhien(m: int, n: int, min_val: int = -50, max_val: int = 100) -> Matrix:
    """Tạo mảng 2 chiều kích thước m x n chứa các số nguyên ngẫu nhiên."""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]

def in_mang(matrix: Matrix) -> None:
    """In mảng 2 chiều ra màn hình với định dạng cột ngay ngắn."""
    if not matrix:
        print("Mảng rỗng!")
        return
    for row in matrix:
        print(" ".join(f"{x:4}" for x in row))

def xuat_dong_k(matrix: Matrix, k: int) -> None:
    """Xuất các phần tử thuộc dòng k."""
    if 0 <= k < len(matrix):
        print(f"Các phần tử thuộc dòng {k}: {matrix[k]}")
    else:
        print(f"Lỗi: Dòng {k} không tồn tại trong mảng.")

def xuat_cot_k(matrix: Matrix, k: int) -> None:
    """Xuất các phần tử thuộc cột k."""
    if matrix and 0 <= k < len(matrix[0]):
        cot = [row[k] for row in matrix]
        print(f"Các phần tử thuộc cột {k}: {cot}")
    else:
        print(f"Lỗi: Cột {k} không tồn tại trong mảng.")

def tim_dong_tong_lon_nhat(matrix: Matrix) -> tuple[int, int]:
    """Tìm dòng có tổng các phần tử lớn nhất. Trả về (chỉ_số_dòng, tổng)."""
    tong_cac_dong = [sum(row) for row in matrix]
    max_sum = max(tong_cac_dong)
    chi_so_dong = tong_cac_dong.index(max_sum)
    return chi_so_dong, max_sum

def tim_cot_tich_nho_nhat(matrix: Matrix) -> tuple[int, int]:
    """Tìm cột có tích các phần tử nhỏ nhất. Trả về (chỉ_số_cột, tích)."""
    m, n = len(matrix), len(matrix[0])
    tich_cac_cot = [math.prod(matrix[i][j] for i in range(m)) for j in range(n)]
    min_prod = min(tich_cac_cot)
    chi_so_cot = tich_cac_cot.index(min_prod)
    return chi_so_cot, min_prod

def xuat_dong_chan_cot_le(matrix: Matrix) -> list[int]:
    """Lấy các phần tử thuộc dòng chẵn (0, 2...) và cột lẻ (1, 3...)."""
    m, n = len(matrix), len(matrix[0])
    ket_qua = [matrix[i][j] for i in range(m) if i % 2 == 0 
                            for j in range(n) if j % 2 != 0]
    return ket_qua

def tbc_phan_tu_chan_dong_le(matrix: Matrix) -> Optional[float]:
    """Tính TBC các phần tử CHẴN nằm trên DÒNG LẺ."""
    m, n = len(matrix), len(matrix[0])
    phan_tu_thoa_man = [matrix[i][j] for i in range(m) if i % 2 != 0 
                                     for j in range(n) if matrix[i][j] % 2 == 0]
    
    if not phan_tu_thoa_man:
        return None 
    return sum(phan_tu_thoa_man) / len(phan_tu_thoa_man)

def tbc_phan_tu_bien(matrix: Matrix) -> Optional[float]:
    """Tính TBC các phần tử nằm ở biên của mảng."""
    m, n = len(matrix), len(matrix[0])
    if m == 0 or n == 0:
        return None

    bien_elements = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                bien_elements.append(matrix[i][j])

    if not bien_elements:
        return None
    return sum(bien_elements) / len(bien_elements)


def hien_thi_menu():
    print("\n" + "="*50)
    print("CHƯƠNG TRÌNH XỬ LÝ MẢNG 2 CHIỀU")
    print("="*50)
    print("1. Tạo mảng a chứa các số nguyên ngẫu nhiên.")
    print("2. Xuất các phần tử thuộc dòng k.")
    print("3. Xuất các phần tử thuộc cột k.")
    print("4. Tìm dòng có tổng lớn nhất.")
    print("5. Tìm cột có tích nhỏ nhất.")
    print("6. Xuất ra các phần tử thuộc dòng chẵn và cột lẻ.")
    print("7. Tính TBC các phần tử chẵn thuộc dòng lẻ.")
    print("8. Tính TBC các phần tử thuộc biên.")
    print("0. Thoát chương trình.")
    print("="*50)


def main():
    a: Matrix = []
    
    while True:
        hien_thi_menu()
        try:
            lua_chon = int(input("Mời bạn chọn chức năng (0-8): "))
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
            continue

        if lua_chon == 0:
            print("Đã thoát chương trình. Tạm biệt!")
            break
            
        if lua_chon != 1 and not a:
            print("Lỗi: Bạn cần tạo mảng (Chọn số 1) trước khi thực hiện các thao tác khác!")
            continue

        match lua_chon:
            case 1:
                try:
                    m = int(input("Nhập số dòng m: "))
                    n = int(input("Nhập số cột n: "))
                    if m <= 0 or n <= 0:
                        print("Kích thước mảng phải lớn hơn 0.")
                        continue
                    a = tao_mang_ngau_nhien(m, n)
                    print("\nĐã tạo mảng thành công:")
                    in_mang(a)
                except ValueError:
                    print("Kích thước mảng phải là số nguyên!")
            
            case 2:
                k = int(input("Nhập chỉ số dòng k cần xuất: "))
                xuat_dong_k(a, k)
                
            case 3:
                k = int(input("Nhập chỉ số cột k cần xuất: "))
                xuat_cot_k(a, k)
                
            case 4:
                chi_so, tong_max = tim_dong_tong_lon_nhat(a)
                print(f"Dòng {chi_so} có tổng lớn nhất là: {tong_max}")
                print(f"Chi tiết dòng {chi_so}: {a[chi_so]}")
                
            case 5:
                chi_so, tich_min = tim_cot_tich_nho_nhat(a)
                print(f"Cột {chi_so} có tích nhỏ nhất là: {tich_min}")
                print(f"Chi tiết cột {chi_so}: {[row[chi_so] for row in a]}")
                
            case 6:
                ket_qua = xuat_dong_chan_cot_le(a)
                print(f"Các phần tử thuộc dòng chẵn và cột lẻ: {ket_qua if ket_qua else 'Không có'}")
                
            case 7:
                tbc = tbc_phan_tu_chan_dong_le(a)
                if tbc is not None:
                    print(f"Trung bình cộng các phần tử chẵn thuộc dòng lẻ: {tbc:.2f}")
                else:
                    print("Không có phần tử chẵn nào nằm trên dòng lẻ!")
                    
            case 8:
                tbc = tbc_phan_tu_bien(a)
                if tbc is not None:
                    print(f"Trung bình cộng các phần tử thuộc biên: {tbc:.2f}")
                else:
                    print("Lỗi tính toán mảng biên!")
                    
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 8.")

if __name__ == "__main__":
    main()