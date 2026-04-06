import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class SinhVien:
    ma_sv: str
    ten: str
    nam_sinh: int
    diem_tb: float

    def __post_init__(self):
        self.ma_sv = self.ma_sv.strip()
        self.ten = self.ten.strip()
        
        if len(self.ma_sv) > 10:
            raise ValueError(f"Mã sinh viên '{self.ma_sv}' vượt quá 10 ký tự.")
        if len(self.ten) > 20:
            raise ValueError(f"Tên sinh viên '{self.ten}' vượt quá 20 ký tự.")
        if not (0.0 <= self.diem_tb <= 10.0):
            raise ValueError(f"Điểm trung bình {self.diem_tb} không hợp lệ (phải từ 0-10).")

def tao_du_lieu_mau() -> List[SinhVien]:
    return [
        SinhVien("02DH0001", "Phan Thị Lan", 2005, 8.5),
        SinhVien("02CD0002", "Nguyễn Văn A", 2006, 4.0), # Hệ cao đẳng, rớt
        SinhVien("01DH0003", "Phan Hoàng Huy", 2004, 5.5),
        SinhVien("03DH0004", "Trần Ngọc Lan", 2006, 9.0),
        SinhVien("01QT0005", "Lê Thị B", 2008, 3.5)
    ]

def dem_sv_len_lop(danh_sach: List[SinhVien]) -> int:
    return sum(1 for sv in danh_sach if sv.diem_tb >= 5.0)

def xuat_sv_du_20_tuoi(danh_sach: List[SinhVien]) -> None:
    nam_hien_tai = datetime.datetime.now().year
    print(f"\n--- Danh sách sinh viên đủ 20 tuổi (Tính đến {nam_hien_tai}) ---")
    
    sv_hop_le = [sv for sv in danh_sach if (nam_hien_tai - sv.nam_sinh) >= 20]
    
    if not sv_hop_le:
        print("Không có sinh viên nào đủ 20 tuổi.")
        return
        
    for sv in sv_hop_le:
        tuoi = nam_hien_tai - sv.nam_sinh
        print(f"Mã SV: {sv.ma_sv:10} | Tên: {sv.ten:20} | Tuổi: {tuoi}")

def dem_sv_he_dai_hoc(danh_sach: List[SinhVien]) -> int:
    return sum(1 for sv in danh_sach if len(sv.ma_sv) >= 4 and sv.ma_sv[2:4].upper() == "DH")

def dem_sv_ten_lan(danh_sach: List[SinhVien]) -> int:
    count = 0
    for sv in danh_sach:
        ten_chinh = sv.ten.split()[-1].lower()
        if ten_chinh == "lan":
            count += 1
    return count

def dem_sv_ho_phan(danh_sach: List[SinhVien]) -> int:
    count = 0
    for sv in danh_sach:
        ho = sv.ten.split()[0].lower()
        if ho == "phan":
            count += 1
    return count

if __name__ == "__main__":
    try:
        danh_sach_sv = tao_du_lieu_mau()
        print(f"Đã tải danh sách gồm {len(danh_sach_sv)} sinh viên.")
        
        so_sv_len_lop = dem_sv_len_lop(danh_sach_sv)
        print(f"Số sinh viên đủ điều kiện lên lớp (ĐTB >= 5): {so_sv_len_lop}")
        
        xuat_sv_du_20_tuoi(danh_sach_sv)
        
        so_sv_dh = dem_sv_he_dai_hoc(danh_sach_sv)
        print(f"\nSố sinh viên hệ Đại học (Mã có chữ DH): {so_sv_dh}")
        
        so_sv_ten_lan = dem_sv_ten_lan(danh_sach_sv)
        print(f"Số sinh viên có tên 'Lan': {so_sv_ten_lan}")
        
        so_sv_ho_phan = dem_sv_ho_phan(danh_sach_sv)
        print(f"Số sinh viên có họ 'Phan': {so_sv_ho_phan}")

    except ValueError as e:
        print(f"Lỗi dữ liệu: {e}")