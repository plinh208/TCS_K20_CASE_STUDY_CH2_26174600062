from datetime import datetime 
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

#du doan ket qua 
#2026-10-22 09:17:25.790762
#<class 'datetime.datetime'>
#2026-10-22 09:17:25
#<class 'str'>
#1:50:00
#<class 'datetime.timedelta'>

#giai thich su khac nhau 
#datetime la dai dien cho mot moc thoi gian cu the (gom ca ngay, thang, nam, gio, phut, giay, micro giay)
#str la mot doan van ban,giong ngay gio nhung may tinh chi hieu no la cac chu cai/ky tu ghep lai, khong the thuc hien cac phep tinh cong tru thoi gian truc tiep
#timedelta la dai dien cho mot khoang thoi gian hoac do lech thoi gian, no sinh ra khi lay 2 moc datetime tru cho nhau hoac dung de cong/tru them thoi gian