from typing import Any
import pprint

he_thong_tai_khoan: dict[str, dict[str, Any]] = {
    "NV001": {
        "ho_ten": "Nguyễn Văn A",
        "chuc_vu": "Trưởng phòng",
        "nam_sinh": 1985,
        "trang_thai_hoat_dong": True
    },
    "NV002": {
        "ho_ten": "Trần Thị B",
        "chuc_vu": "Chuyên viên",
        "nam_sinh": 1992,
        "trang_thai_hoat_dong": True
    },
    "NV003": {
        "ho_ten": "Lê Văn C",
        "chuc_vu": "Thực tập sinh",
        "nam_sinh": 2002,
        "trang_thai_hoat_dong": False
    }
}

if __name__ == "__main__":
    print("--- Dữ liệu gốc trong hệ thống ---")
    pprint.pprint(he_thong_tai_khoan, sort_dicts=False)

    print("\n--- Truy xuất dữ liệu cụ thể ---")
    ten_nv002 = he_thong_tai_khoan.get("NV002", {}).get("ho_ten", "Không tìm thấy")
    print(f"Tên của nhân viên NV002 là: {ten_nv002}")