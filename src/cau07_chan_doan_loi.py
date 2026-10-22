ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Đien nang: {dien_nang_kwh:.3f} kWh")
      #lan 1 gap loi SyntaxError: '(' was never closed tai dong in dien nang 
      #nguyen nhan go nham thieu dau ngoac don ')' trong cum (f"Điện năng: {dien_nang:.3f} kWh"
      #cach sua go them dau ngoac don ')' 
#lan 2 gap loi TypeError: unsupported operand type(s) for /: 'str' and 'int' tai dong dien_nang_kwh 
#nguyen nhan do thieu ham float() o dong 2 nen bien cong_suat_w nhan kieu str, khong chia duoc cho kieu int o dong 4
#cach sua them float vao dong so 2 bao quanh ipnut
#lan 3 gap loi  name 'dien_nang' is not defined. Did you mean: 'dien_nang_kwh'?
#nguyen nhan go sai ten bien 'dien_nang' thay vi 'dien_nang_kwh' o dong so 6 
# cach sua 'dien_nang:.3f' thanh 'dien_nang_kwh' 
