# Cho truoc cac gia tri:
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# Tinh dien nang tieu thu va chi phi dien theo cong thuc cho san
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

#In ca gia tri va kieu du lieu cua hai ket qua
print("--- Ket qua ---")
print("Dien nang tieu thu (kWh):", dien_nang_kwh, "| Kieu:", type(dien_nang_kwh))
print("Chi phi dien (VND):", chi_phi, "| Kieu:", type(chi_phi))

# Du doan:
# dien_nang_kwh = 250 * 90 / 60 / 1000 = 22500 / 60 / 1000 = 375 / 1000 = 0.375
# chi_phi = 0.375 * 3000 = 1125.0

# Thay so_phut bang 60 roi chay lai va so sanh
print("\n--- Ket qua (Khi so_phut = 60) ---")
so_phut_moi = 60
dien_nang_moi = cong_suat_w * so_phut_moi / 60 / 1000
chi_phi_moi = dien_nang_moi * don_gia_kwh

print("Dien nang moi (kWh):", dien_nang_moi)
print("Chi phi moi (VND):", chi_phi_moi)
print("So sanh: Khi giam thoi gian tu 90 phut xuong 60 phut, dien nang va chi phi deu giam.")