# BÀI 5: ĐỌC FILE VĂN BẢN CÓ SẴN VÀ THỐNG KÊ DỮ LIỆU

def doc_file_sinhvien(filename='danh_sach_sinh_vien.csv'):
    """Đọc file danh_sach_sinh_vien.csv và chuyển thành danh sách sinh viên"""
    danh_sach = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f"Đang đọc file: {filename} ...\n")
            for dong in f:
                dong = dong.strip()
                if dong and not dong.startswith('#'):  # bỏ dòng trống và comment
                    parts = [p.strip() for p in dong.split(',')]
                    if len(parts) == 3:
                        ma_sv = parts[0]
                        ho_ten = parts[1]
                        try:
                            diem = float(parts[2])
                            danh_sach.append((ma_sv, ho_ten, diem))
                        except ValueError:
                            print(f"⚠️ Lỗi điểm số ở dòng: {dong}")
        return danh_sach
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file '{filename}'!")
        print("Vui lòng kiểm tra file danh_sach_sinh_vien.csv có tồn tại trong cùng thư mục không.")
        return []
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        return []


def thong_ke(danh_sach):
    """Thống kê dữ liệu sinh viên"""
    if not danh_sach:
        return None
    
    so_luong = len(danh_sach)
    tong_diem = sum(sv[2] for sv in danh_sach)
    diem_trung_binh = tong_diem / so_luong if so_luong > 0 else 0
    
    so_dat = sum(1 for sv in danh_sach if sv[2] >= 5.0)
    so_khong_dat = so_luong - so_dat
    
    return {
        'so_luong': so_luong,
        'diem_trung_binh': diem_trung_binh,
        'so_dat': so_dat,
        'so_khong_dat': so_khong_dat
    }


def ghi_bao_cao(thong_ke_data, danh_sach, output_file='baocao.txt'):
    """Ghi kết quả thống kê ra file baocao.txt"""
    if not thong_ke_data:
        print("Không có dữ liệu để ghi báo cáo!")
        return
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("BÁO CÁO THỐNG KÊ SINH VIÊN\n")
        f.write("="*55 + "\n")
        f.write(f"Tổng số sinh viên          : {thong_ke_data['so_luong']}\n")
        f.write(f"Điểm trung bình            : {thong_ke_data['diem_trung_binh']:.2f}\n")
        f.write(f"Số sinh viên đạt (>= 5.0)  : {thong_ke_data['so_dat']}\n")
        f.write(f"Số sinh viên không đạt     : {thong_ke_data['so_khong_dat']}\n")
        f.write("="*55 + "\n\n")
        
        f.write("DANH SÁCH CHI TIẾT:\n")
        f.write(f"{'Mã SV':<8} {'Họ và tên':<28} {'Điểm':<6} {'Trạng thái'}\n")
        f.write("-"*65 + "\n")
        
        for sv in danh_sach:
            trang_thai = "Đạt" if sv[2] >= 5.0 else "Không đạt"
            f.write(f"{sv[0]:<8} {sv[1]:<28} {sv[2]:<6.1f} {trang_thai}\n")
    
    print(f"✓ Đã ghi báo cáo thành công vào file: **{output_file}**")


# ===================== CHƯƠNG TRÌNH CHÍNH =====================
if __name__ == "__main__":
    print("=== BÀI 5: ĐỌC FILE danh_sach_sinh_vien.csv CÓ SẴN VÀ THỐNG KÊ ===\n")
    
    # Đọc file có sẵn
    ds_sinhvien = doc_file_sinhvien('danh_sach_sinh_vien.csv')
    
    if ds_sinhvien:
        print(f"✅ Đọc thành công {len(ds_sinhvien)} sinh viên từ file.\n")
        
        ket_qua = thong_ke(ds_sinhvien)
        ghi_bao_cao(ket_qua, ds_sinhvien)
        
        # Hiển thị báo cáo trên màn hình
        print("\n" + "="*65)
        print("NỘI DUNG BÁO CÁO (baocao.txt):")
        print("="*65)
        try:
            with open('baocao.txt', 'r', encoding='utf-8') as f:
                print(f.read())
        except:
            print("Không thể đọc lại file baocao.txt")
    else:
        print("\nChương trình kết thúc do không có dữ liệu.")
    
