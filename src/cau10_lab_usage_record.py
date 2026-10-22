from datetime import datetime
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
thoi_gian_phut = float(input("Nhập thời gian sử dụng (phút): "))
don_gia_dien = float(input("Nhập đơn giá điện (VND/kWh): "))

dien_nang_kwh = (cong_suat_w / 1000) * (thoi_gian_phut / 60)
chi_phi_vnd = dien_nang_kwh * don_gia_dien
tren_60_phut = thoi_gian_phut > 60
thoi_diem_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n--- ket qua  ---")
print(f"ma phien: {ma_phien}")
print(f"may: {ma_may}")
print(f"con suat: {cong_suat_w:.2f} W")
print(f"thoi luong: {thoi_gian_phut:.0f} phút")
print(f"dien nang: {dien_nang_kwh:.3f} kWh")
print(f"chi phi: {chi_phi_vnd:.2f} VND")
print(f"tran 60 phut: {tren_60_phut}")
print(f"ghi nhan luc: {thoi_diem_hien_tai}")