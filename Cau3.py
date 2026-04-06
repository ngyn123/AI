#Cau 3
import re
chuoi = "               Hello                            World "
chuoi1 = re.sub(r'\s+', ' ', chuoi.strip())
chuoi2 = chuoi1.replace('H', 'J')
print(chuoi2)