#Cau 13
from itertools import zip_longest

def merge_and_sum_arrays(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip_longest(a, b, fillvalue=0)]

if __name__ == "__main__":
    mang_a = [3, 9, 1, 4]
    mang_b = [2, 7, 4, 3, 2, 8]

    ket_qua = merge_and_sum_arrays(mang_a, mang_b)
    print("Mảng a:      ", mang_a)
    print("Mảng b:      ", mang_b)
    print("Mảng kết quả:", ket_qua)