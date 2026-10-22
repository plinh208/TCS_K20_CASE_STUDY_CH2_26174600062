ma_phien = input("nhap_ma_phien ")
ma_may = input("nhap_ma_may ")

cong_suat = float(input("nhap_cong_suat "))
so_phut = int(input("nhap_so_phut "))
don_gia = float(input("nhap_don_gia "))

dien_nang_kwh = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia

print("\n--- ket_qua_dau_ra ---")
print("Ma phien:", ma_phien)
print("May:", ma_may)
print("Dien nang:", dien_nang_kwh)
print("Chi phi:", chi_phi)