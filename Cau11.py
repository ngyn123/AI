#Cau 11
import random
from typing import List, Tuple
n = int(input("Nhap n: "))
a = [random.randint(1,100) for _ in range(n)]
b = [x for x in a if x % 2 == 0]
print(f"a = {a}")
print(f"b = {b}")