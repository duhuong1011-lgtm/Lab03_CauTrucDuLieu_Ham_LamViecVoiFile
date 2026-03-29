# BÀI 3: SỬ DỤNG LIST COMPREHENSION VÀ DICT COMPREHENSION ĐỂ XỬ LÝ DỮ LIỆU
# Dữ liệu mẫu
diem = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

print("Danh sách điểm gốc:", diem)
print("-" * 70)
# 1. Tạo danh sách mới chỉ gồm các điểm đạt (>= 5) - List Comprehension
diem_dat = [d for d in diem if d >= 5]

print("1. Danh sách điểm ĐẠT (>= 5):")
print(diem_dat)
# 2. Tạo danh sách bình phương của các điểm đạt - List Comprehension
binh_phuong = [d**2 for d in diem if d >= 5]

print("\n2. Bình phương của các điểm đạt:")
print(binh_phuong)
# 3. Tạo từ điển xếp loại bằng Dict Comprehension
xep_loai = {
    i+1: ("A" if d >= 8 else 
          "B" if d >= 6.5 else 
          "C" if d >= 5 else "F")
    for i, d in enumerate(diem)
}

print("\n3. Từ điển xếp loại theo số thứ tự sinh viên:")
for stt, loai in xep_loai.items():
    print(f"Sinh viên {stt:2d}: Điểm = {diem[stt-1]:>4} → Xếp loại: {loai}")

# In tóm tắt số lượng theo từng loại
print("\nTóm tắt số lượng xếp loại:")
from collections import Counter
dem_loai = Counter(xep_loai.values())
for loai, so_luong in sorted(dem_loai.items()):
    print(f"Xếp loại {loai}: {so_luong} sinh viên")
