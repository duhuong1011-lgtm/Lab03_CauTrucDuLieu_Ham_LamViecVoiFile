 #BÀI 2: THỐNG KÊ DỮ LIỆU BẰNG DICT VÀ SET
du_lieu = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

print("Dữ liệu gốc:", du_lieu)
print("-" * 50)
# 1. Loại bỏ phần tử trùng lặp bằng set
mon_hoc_unique = set(du_lieu)

print("1. Môn học sau khi loại bỏ trùng lặp (sử dụng set):")
print(mon_hoc_unique)
print(f"Số môn học duy nhất: {len(mon_hoc_unique)}\n")
# 2. Đếm số lần xuất hiện của từng môn học bằng dict
dem_mon_hoc = {}
for mon in du_lieu:
    if mon in dem_mon_hoc:
        dem_mon_hoc[mon] += 1
    else:
        dem_mon_hoc[mon] = 1

print("2. Số lần xuất hiện của từng môn học (sử dụng dict):")
for mon, so_lan in dem_mon_hoc.items():
    print(f"• {mon:<8}: {so_lan} lần")

# 3. In ra môn học được đăng ký nhiều nhất
if dem_mon_hoc:
    mon_nhieu_nhat = max(dem_mon_hoc, key=dem_mon_hoc.get)
    print(f"\n3. Môn học được đăng ký nhiều nhất: **{mon_nhieu_nhat}** ({dem_mon_hoc[mon_nhieu_nhat]} lần)")

# 4. Sắp xếp kết quả đếm theo số lần giảm dần
print("\n4. Danh sách môn học sắp xếp theo số lần đăng ký GIẢM DẦN:")
sap_xep = sorted(dem_mon_hoc.items(), key=lambda x: x[1], reverse=True)

for mon, so_lan in sap_xep:
    print(f"• {mon:<8}: {so_lan} lần")

