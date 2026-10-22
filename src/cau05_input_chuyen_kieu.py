print("---  Nhap du lieu ---")
ma_may = input("Nhap ma may : ")
print("Kieu du lieu ma_may:", type(ma_may))

cong_suat_str = input("Nhap cong suat W : ")
print("Kieu du lieu cong_suat_str:", type(cong_suat_str))

so_phut_str = input("Nhap so phut su dung : ")
print("Kieu du lieu so_phut_str:", type(so_phut_str))

don_gia_str = input("Nhap don gia dien/kWh : ")
print("Kieu du lieu don_gia_str:", type(don_gia_str))

cong_suat = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

print("\n--- Kieu du lieu sau khi chuyen doi ---")
print("Kieu cong_suat:", type(cong_suat))
print("Kieu so_phut:", type(so_phut))
print("Kieu don_gia_kwh:", type(don_gia_kwh))

dien_nang_kwh = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Ket qua  ---")
print("Ma may:", ma_may)
print("Dien nang tieu thu (kWh):", dien_nang_kwh)
print("Chi phi dien (VND):", chi_phi)