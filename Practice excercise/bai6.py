# Tạo các đối tượng (class) cho một hệ thống xuất hóa đơn của một cửa hàng tạp hóa.Hệ thống bao gồm
# các đối tượng sau:
# Khách hàng (mã khách hàng, giới tính, độ tuổi)
# Nhân viên bán hàng (mã nv, giới tính, ngày làm việc, ca đăng ký)
# Nhân viên nhập hàng (mã nv, giới tính, ngày làm việc, thâm niên)
# Mặt hàng (mã hàng hóa, tên hàng hóa, phân loại, giá)
# Hóa đơn (mã hóa đơn, mã nv bán hàng, mã KH nếu có, danh sách mặt hàng, tổng giá, ngày mua)
class khachHang:
    def __init__(self, ten, gioiTinh, tuoi):
        self.ten= ten
        self.gioiTinh= gioiTinh
        self.tuoi= tuoi

class nvBanHang:
    def __init__(self, ten, gioiTinh, ngayLamViec,thamNien):
        self.ten= ten
        self.gioiTinh= gioiTinh
        self.ngayLamViec= None
        self.thamNien= thamNien
class nvMuaHang:
    def __init__(self, ten, gioiTinh, ngayLamViec,thamNien):
        self.ten= ten
        self.gioiTinh= gioiTinh
        self.ngayLamViec= None
        self.thamNien= thamNien
class matHang:
    
