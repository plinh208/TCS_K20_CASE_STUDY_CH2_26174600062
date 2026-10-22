#tong thoi gian su dung la 135 phut va cac bien:
tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60

print("--- Ket qua  ---")
print("So gio tron ven:", so_gio)
print("So phut con lai:", so_phut_con_lai)

su_dung_lau = tong_phut > 60

print("\n--- Ket qua ---")
print("Su dung lau:", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)

print("\n--- Ket qua  ---")
print("Du lieu hop le:", du_lieu_hop_le)

# Du doan: 100 + 20 * 3 = 100 + 60 = 160 (nhan chia truoc, cong tru sau)
# Du doan: (100 + 20) * 3 = 120 * 3 = 360 (tinh trong ngoac truoc)
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3

print("\n--- Ket qua  ---")
print("Gia tri bieu thuc 1:", bieu_thuc_1)
print("Gia tri bieu thuc 2:", bieu_thuc_2)