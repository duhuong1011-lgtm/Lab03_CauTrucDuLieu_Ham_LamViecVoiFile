 #BÀI 6: ĐỌC FILE CSV VÀ XỬ LÝ LỖI 
import csv
# Danh sách lưu dữ liệu hợp lệ và lỗi
danh_sach_hop_le = []
danh_sach_loi = []
# 1. Đọc file CSV
try:
    with open('danh_sach_sinh_vien.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Đọc dòng tiêu đề (header)
        header = next(reader, None)
        print(f"Tiêu đề file: {header}\n")
        
        print("Đang đọc dữ liệu từ file danh_sach_sinh_vien.csv...\n")
        
        for i, row in enumerate(reader, 1):   # i bắt đầu từ 1
            if len(row) < 3:                  # Nếu thiếu cột
                danh_sach_loi.append((i, row, "Thiếu cột dữ liệu"))
                print(f"Dòng {i}: Thiếu cột dữ liệu → {row}")
                continue
            
            ma_sv = row[0].strip()
            ho_ten = row[1].strip()
            diem_str = row[2].strip()
            
            try:
                # Kiểm tra điểm có phải là số không
                diem = float(diem_str)
                
                # Kiểm tra điểm có nằm trong khoảng 0-10 không
                if 0 <= diem <= 10:
                    danh_sach_hop_le.append((ma_sv, ho_ten, diem))
                else:
                    danh_sach_loi.append((i, row, f"Điểm ngoài khoảng (0-10): {diem}"))
                    print(f"Dòng {i}: Điểm ngoài khoảng 0-10 → {diem}")
                    
            except ValueError:
                # Điểm không phải là số
                danh_sach_loi.append((i, row, f"Điểm không phải số: '{diem_str}'"))
                print(f"Dòng {i}: Điểm không phải số → '{diem_str}'")
                
except FileNotFoundError:
    print("❌ Không tìm thấy file 'danh_sach_sinh_vien.csv'!")
    print("Vui lòng đặt file danh_sach_sinh_vien.csv vào cùng thư mục với code.")
    exit()
except Exception as e:
    print(f"Lỗi khi đọc file: {e}")
    exit()

# 2. Hiển thị kết quả đọc file
print("\n" + "="*60)
print(f"Đọc xong file. Tổng số dòng dữ liệu: {len(danh_sach_hop_le) + len(danh_sach_loi)}")
print(f"Số dòng hợp lệ : {len(danh_sach_hop_le)}")
print(f"Số dòng lỗi    : {len(danh_sach_loi)}")
print("="*60)

# 3. Tính điểm trung bình của dữ liệu hợp lệ
if danh_sach_hop_le:
    tong_diem = sum(sv[2] for sv in danh_sach_hop_le)
    diem_trung_binh = tong_diem / len(danh_sach_hop_le)
    
    print(f"\nĐiểm trung bình của {len(danh_sach_hop_le)} sinh viên hợp lệ: {diem_trung_binh:.2f}")
else:
    print("\nKhông có dữ liệu hợp lệ để tính điểm trung bình.")

# 4. Ghi các dòng lỗi vào file loi.txt
if danh_sach_loi:
    with open('loi.txt', 'w', encoding='utf-8') as f:
        f.write("DANH SÁCH CÁC DÒNG LỖI TRONG FILE CSV\n")
        f.write("="*60 + "\n")
        f.write(f"{'Dòng':<6} {'Mã SV':<8} {'Họ tên':<25} {'Điểm':<10} {'Lý do lỗi'}\n")
        f.write("-"*70 + "\n")
        
        for dong, row, ly_do in danh_sach_loi:
            ma = row[0] if len(row) > 0 else ""
            ten = row[1] if len(row) > 1 else ""
            diem = row[2] if len(row) > 2 else ""
            f.write(f"{dong:<6} {ma:<8} {ten:<25} {diem:<10} {ly_do}\n")
    
    print(f"✓ Đã ghi {len(danh_sach_loi)} dòng lỗi vào file 'loi.txt'")
else:
    print("Không có lỗi nào được ghi nhận.")

