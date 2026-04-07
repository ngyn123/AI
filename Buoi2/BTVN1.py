from typing import List

def tron_mang_min(a: List[int], b: List[int]) -> List[int]:
    """
    Trộn 2 mảng một chiều, lấy giá trị nhỏ hơn ở mỗi vị trí tương ứng.
    Các phần tử dư thừa ở mảng dài hơn sẽ được đưa thẳng vào mảng kết quả.
    """
    ket_qua = [min(x, y) for x, y in zip(a, b)]
    
    ket_qua.extend(a[len(b):])
    ket_qua.extend(b[len(a):])
    
    return ket_qua

if __name__ == "__main__":
    mang_a = [3, 9, 1, 4]
    mang_b = [2, 7, 4, 3, 2, 8]
    
    mang_ket_qua = tron_mang_min(mang_a, mang_b)
    
    print(f"Mảng a:       {mang_a}")
    print(f"Mảng b:       {mang_b}")
    print(f"Mảng kết quả: {mang_ket_qua}")