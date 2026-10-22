# Tao cac bien phu hop theo quy tac snake_case
# Chon kieu du lieu phu hop (str, int, float, bool, NoneType)
ma_phien = "LAB026"          # Kieu str
ma_may = "PC12"              # Kieu str
cong_suat = 250.0            # Kieu float
thoi_gian = 90               # Kieu int
trang_thai = True            # Kieu bool
ghi_chu = None               # Kieu NoneType

# In tung gia tri va dung type() de kiem tra kieu
print("--- Ket qua  ---")
print("Ma phien:", ma_phien, "| Kieu du lieu:", type(ma_phien))
print("Ma may:", ma_may, "| Kieu du lieu:", type(ma_may))
print("Cong suat:", cong_suat, "| Kieu du lieu:", type(cong_suat))
print("Thoi gian:", thoi_gian, "| Kieu du lieu:", type(thoi_gian))
print("Trang thai:", trang_thai, "| Kieu du lieu:", type(trang_thai))
print("Ghi chu:", ghi_chu, "| Kieu du lieu:", type(ghi_chu))

# Thay thoi gian su dung tu 90 thanh 120 bang phep gan lai va in gia tri moi
print("\n--- Ket qua  ---")
thoi_gian = 120
print("Thoi gian su dung moi sau khi gan lai:", thoi_gian)