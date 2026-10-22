from datetime import datetime

ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
thoi_luong_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VND/kWh): "))

so_gio = thoi_luong_phut // 60
so_phut_le = thoi_luong_phut % 60
dien_nang_kwh = cong_suat_w * thoi_luong_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

tren_60_phut = thoi_luong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (thoi_luong_phut > 0) and (don_gia_kwh > 0)
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {thoi_luong_phut} phút ({so_gio} giờ {so_phut_le} phút)")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Dữ liệu hợp lệ: {du_lieu_hop_le}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")
