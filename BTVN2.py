from typing import TypeAlias, List

Matrix: TypeAlias = list[list[int]]


def kiem_tra_ma_tran_vuong(a: Matrix) -> int:
    """Kiểm tra ma trận có vuông không và trả về cấp n. Bắn lỗi nếu không vuông."""
    if not a:
        raise ValueError("Ma trận rỗng.")
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Ma trận không phải là ma trận vuông cấp n x n.")
    return n

def tong_tam_giac_tren_cheo_phu(a: Matrix) -> int:
    """a. Tính tổng tam giác trên của đường chéo phụ (bao gồm cả đường chéo phụ)."""
    n = kiem_tra_ma_tran_vuong(a)
    return sum(a[i][j] for i in range(n) for j in range(n) if i + j <= n - 1)

def la_ma_tran_doi_xung(a: Matrix) -> bool:
    """e. Kiểm tra ma trận đối xứng qua đường chéo chính (a[i][j] == a[j][i])."""
    n = kiem_tra_ma_tran_vuong(a)
    return all(a[i][j] == a[j][i] for i in range(n) for j in range(i + 1, n))

def cheo_chinh_tang_dan(a: Matrix) -> bool:
    """f. Kiểm tra đường chéo chính có tăng dần nghiêm ngặt hay không."""
    n = kiem_tra_ma_tran_vuong(a)
    return all(a[i][i] < a[i + 1][i + 1] for i in range(n - 1))

def xuat_tam_giac_duoi_cheo_phu(a: Matrix) -> List[int]:
    """g. Trích xuất các phần tử tam giác dưới đường chéo phụ (gồm cả chéo phụ)."""
    n = kiem_tra_ma_tran_vuong(a)
    ket_qua = [a[i][j] for i in range(n) for j in range(n) if i + j >= n - 1]
    print(f"Các phần tử thuộc tam giác dưới chéo phụ: {ket_qua}")
    return ket_qua

def cheo_phu_giam_dan(a: Matrix) -> bool:
    """h. Kiểm tra đường chéo phụ có giảm dần nghiêm ngặt hay không."""
    n = kiem_tra_ma_tran_vuong(a)
    return all(a[i][n - 1 - i] > a[i + 1][n - 1 - (i + 1)] for i in range(n - 1))



def am_sang_tuyet_doi(a: Matrix) -> None:
    """b. Chuyển các phần tử âm thành trị tuyệt đối (Sửa đổi trực tiếp mảng gốc)."""
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] < 0:
                a[i][j] = abs(a[i][j])

def thay_the_phan_tu_chan(a: Matrix, x: int) -> None:
    """c. Thay các phần tử chẵn bằng giá trị x (Sửa đổi trực tiếp mảng gốc)."""
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] % 2 == 0:
                a[i][j] = x

def kiem_tra_toan_chan(a: Matrix) -> bool:
    """d. Kiểm tra mảng có chứa toàn số chẵn hay không."""
    return all(phan_tu % 2 == 0 for row in a for phan_tu in row)


if __name__ == "__main__":
    ma_tran_test = [
        [-2, 4, 1],
        [8, -5, 3],
        [6, 7, 9]
    ]
    
    print("Ma trận ban đầu:")
    for row in ma_tran_test:
        print(row)
        
    print(f"\na. Tổng tam giác trên chéo phụ: {tong_tam_giac_tren_cheo_phu(ma_tran_test)}")
    print(f"e. Là ma trận đối xứng?: {la_ma_tran_doi_xung(ma_tran_test)}")
    print(f"f. Đường chéo chính tăng dần?: {cheo_chinh_tang_dan(ma_tran_test)}") 
    
    xuat_tam_giac_duoi_cheo_phu(ma_tran_test)
    
    print(f"h. Đường chéo phụ giảm dần?: {cheo_phu_giam_dan(ma_tran_test)}")
    print(f"d. Mảng toàn bộ là số chẵn?: {kiem_tra_toan_chan(ma_tran_test)}")
    
    print("\nThực hiện thay đổi mảng (In-place mutation)...")
    am_sang_tuyet_doi(ma_tran_test)
    print("b. Sau khi chuyển phần tử âm thành tuyệt đối:")
    for row in ma_tran_test: print(row)
        
    thay_the_phan_tu_chan(ma_tran_test, 99)
    print("\nc. Sau khi thay số chẵn bằng 99:")
    for row in ma_tran_test: print(row)