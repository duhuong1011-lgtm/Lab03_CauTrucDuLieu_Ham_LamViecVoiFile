import csv
# 1. Tạo danh sách ít nhất 8 sinh viên, mỗi sinh viên là một tuple (mã SV, họ tên, điểm)
danh_sach_sinh_vien = [
    ("SV001", "Nguyễn Văn An", 7.5),
    ("SV002", "Trần Thị Bình", 8.0),
    ("SV003", "Lê Hoàng Cường", 9.2),
    ("SV004", "Phạm Minh Dũng", 6.8),
    ("SV005", "Hoàng Thị Lan", 8.5),
    ("SV006", "Đặng Quang Minh", 7.0),
    ("SV007", "Vũ Thị Ngọc", 9.5),
    ("SV008", "Bùi Văn Hải", 8.3),
    ("SV009", "Phan Thị Thu", 9.0),
    ("SV010", "Lý Minh Quân", 7.8)
]
# 2. In toàn bộ danh sách sinh viên
print("1. TOÀN BỘ DANH SÁCH SINH VIÊN:")
print("-" * 60)
for sv in danh_sach_sinh_vien:
    print(f"Mã SV: {sv[0]:<6} | Họ tên: {sv[1]:<22} | Điểm: {sv[2]:>5}")
print("-" * 60)

# 3. Tìm sinh viên có điểm cao nhất
sinh_vien_max = max(danh_sach_sinh_vien, key=lambda x: x[2])
print("\n2. SINH VIÊN CÓ ĐIỂM CAO NHẤT:")
print(f"Mã SV: {sinh_vien_max[0]} | Họ tên: {sinh_vien_max[1]} | Điểm: {sinh_vien_max[2]}")

# 4. Tính điểm trung bình của cả lớp
tong_diem = sum(sv[2] for sv in danh_sach_sinh_vien)
so_luong = len(danh_sach_sinh_vien)
diem_trung_binh = tong_diem / so_luong

print(f"\n3. ĐIỂM TRUNG BÌNH CỦA CẢ LỚP: {diem_trung_binh:.2f}")

# 5. In danh sách sinh viên có điểm lớn hơn hoặc bằng 8
print("\n4. DANH SÁCH SINH VIÊN CÓ ĐIỂM >= 8:")
print("-" * 60)
for sv in danh_sach_sinh_vien:
    if sv[2] >= 8.0:
        print(f"Mã SV: {sv[0]:<6} | Họ tên: {sv[1]:<22} | Điểm: {sv[2]:>5}")
print("-" * 60)

# ==================== PHẦN LÀM VIỆC VỚI FILE CSV ====================

print("\n=== TẠO VÀ GHI DỮ LIỆU RA FILE CSV ===")

# Ghi dữ liệu ra file CSV
with open('danh_sach_sinh_vien.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Viết tiêu đề
    writer.writerow(['MaSV', 'HoTen', 'Diem'])
    # Viết dữ liệu
    writer.writerows(danh_sach_sinh_vien)

print("✓ Đã tạo và ghi file 'danh_sach_sinh_vien.csv' thành công!")

# Đọc lại file CSV để kiểm tra
print("\n=== NỘI DUNG FILE CSV VỪA TẠO ===")
with open('danh_sach_sinh_vien.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            print(f"{'Tiêu đề':<30} → {row}")
        else:
            print(f"Sinh viên {i:<2} → Mã: {row[0]:<6} | Tên: {row[1]:<20} | Điểm: {row[2]}")

print("\n" + "="*70)
print("="*70)