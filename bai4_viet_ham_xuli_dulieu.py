# BÀI 4: VIẾT HÀM XỬ LÝ DỮ LIỆU SINH VIÊN

def nhap_danh_sach():
    """Hàm nhập danh sách sinh viên từ bàn phím"""
    ds = []
    print("=== NHẬP DANH SÁCH SINH VIÊN ===")
    print("Nhập 'x' để dừng việc nhập.\n")
    
    while True:
        ma_sv = input("Nhập mã sinh viên (hoặc 'x' để dừng): ").strip()
        if ma_sv.lower() == 'x':
            break
        if not ma_sv:
            print("Mã sinh viên không được để trống!")
            continue
            
        ho_ten = input("Nhập họ và tên: ").strip()
        while True:
            try:
                diem = float(input("Nhập điểm: "))
                if 0 <= diem <= 10:
                    break
                else:
                    print("Điểm phải nằm trong khoảng 0 - 10!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
        
        ds.append((ma_sv, ho_ten, diem))
        print(f"✓ Đã thêm sinh viên {ma_sv}\n")
    
    return ds


def tinh_diem_trung_binh(ds):
    """Hàm tính điểm trung bình của danh sách sinh viên"""
    if not ds:
        return 0
    tong_diem = sum(sv[2] for sv in ds)
    return tong_diem / len(ds)


def tim_sv_max(ds):
    """Hàm tìm sinh viên có điểm cao nhất"""
    if not ds:
        return None
    return max(ds, key=lambda x: x[2])


def xep_loai(diem):
    """Hàm trả về xếp loại dựa trên điểm số"""
    if diem >= 8.0:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5.0:
        return "C"
    else:
        return "F"


def in_bao_cao(ds):
    """Hàm in báo cáo tổng hợp"""
    if not ds:
        print("Danh sách sinh viên trống!")
        return
    
    print("\n" + "="*70)
    print("                  BÁO CÁO TỔNG HỢP DANH SÁCH SINH VIÊN")
    print("="*70)
    
    print(f"{'STT':<4} {'Mã SV':<8} {'Họ và tên':<25} {'Điểm':<6} {'Xếp loại':<8}")
    print("-" * 70)
    
    for i, sv in enumerate(ds, 1):
        ma, ten, diem = sv
        loai = xep_loai(diem)
        print(f"{i:<4} {ma:<8} {ten:<25} {diem:<6.1f} {loai:<8}")
    
    print("-" * 70)
    diem_tb = tinh_diem_trung_binh(ds)
    sv_max = tim_sv_max(ds)
    
    print(f"Tổng số sinh viên     : {len(ds)}")
    print(f"Điểm trung bình       : {diem_tb:.2f}")
    print(f"Sinh viên có điểm cao nhất: {sv_max[1]} ({sv_max[0]}) - {sv_max[2]} điểm")
    print("="*70)


# ===================== CHƯƠNG TRÌNH CHÍNH =====================
if __name__ == "__main__":
    
    # Gọi hàm nhập danh sách
    danh_sach = nhap_danh_sach()
    
    # Nếu có dữ liệu thì in báo cáo
    if danh_sach:
        in_bao_cao(danh_sach)
    else:
        print("Không có sinh viên nào được nhập!")
    
