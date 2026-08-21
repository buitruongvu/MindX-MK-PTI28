# Lớp đại diện cho một bộ phim
class Phim:
  def __init__(self, ma_phim, ten_phim, ngay_phat_hanh, diem_danh_gia, duong_link):
    self.ma_phim = ma_phim
    self.ten_phim = ten_phim
    self.ngay_phat_hanh = ngay_phat_hanh # Sử dụng định dạng YYYY-MM-DD để dễ dàng cho việc sắp xếp ngày tháng
    self.diem_danh_gia = diem_danh_gia
    self.duong_link = duong_link
  def cap_nhat(self, ten_phim = None, ngay_phat_hanh=None, diem_danh_gia=None, duong_link=None):
    if ten_phim is not None:
      self.ten_phim = ten_phim
    if ngay_phat_hanh is not None:
      self.ngay_phat_hanh = ngay_phat_hanh
    if diem_danh_gia is not None:
      self.diem_danh_gia = diem_danh_gia
    if duong_link is not None:
      self.duong_link = duong_link
  def __str__(self):
    return f"Mã phim: {self.ma_phim} | Tên phim: {self.ten_phim} | Ngày phát hành: {self.ngay_phat_hanh} | Điểm đánh giá: {self.diem_danh_gia} | Đường link: {self.duong_link}"
# Lớp đại diện cho quản lý danh sách phim
class DanhSachPhim:
  def __init__(self):
    self.danh_sach = []
  #1. Thêm bộ phim mới vào danh sách phim
  def them_phim(self, phim):
    self.danh_sach.append(phim)
    print(f"[*] Đã thêm phim: {phim.ten_phim}")
  #2. Xoá bộ phim khỏi danh sách theo tên
  def xoa_phim(self, ten_phim):
    phim_can_xoa = [p for p in self.danh_sach if p.ten_phim.lower() == ten_phim.lower()]
    if phim_can_xoa:
      for p in phim_can_xoa:
        self.danh_sach.remove(p)
      print(f"Đã xoá phim có tên: {ten_phim}")
    else:
      print(f"Không tìm thấy phim {ten_phim} để xoá")
  # Phương thức phụ trợ in danh sách
  def hien_thi(self):
    if not self.danh_sach:
      print("Danh sách phim hiện đang trống.")
    else:
      print("-" * 80)
      for p in self.danh_sach:
        print(p)
        print("-" * 80)
  #  Tìm kiếm phim theo tên (hỗ trợ tìm kiếm tương đối)
  def tim_kiem(self, tu_khoa):
      ket_qua = [p for p in self.danh_sach if tu_khoa.lower() in p.ten_phim.lower()]
      return ket_qua

    # Sắp xếp danh sách
  def sap_xep_theo_ten(self, tang_dan=True):
      self.danh_sach.sort(key=lambda p: p.ten_phim, reverse=not tang_dan)

  def sap_xep_theo_diem(self, tang_dan=False): # Mặc định điểm xếp từ cao xuống thấp
      self.danh_sach.sort(key=lambda p: p.diem_danh_gia, reverse=not tang_dan)

  def sap_xep_theo_ngay(self, tang_dan=True):
      # Yêu cầu định dạng ngày truyền vào là YYYY-MM-DD để sort chuỗi chính xác
      self.danh_sach.sort(key=lambda p: p.ngay_phat_hanh, reverse=not tang_dan)

# Khởi tạo đối tượng quản lý
ql_phim = DanhSachPhim() 

p1 = Phim("P01", "Inception", "2010-07-16", 8.8, "link/inception")
print(p1)
p1.cap_nhat(ten_phim="Inceptions")
p2 = Phim("P02", "Interstellar", "2014-11-07", 8.6, "link/interstellar")
p3 = Phim("P03", "Avatar", "2009-12-18", 7.9, "link/avatar")
p4 = Phim("P04", "The Dark Knight", "2008-07-18", 9.0, "link/darkknight")

ql_phim.them_phim(p1)
ql_phim.them_phim(p2)
ql_phim.them_phim(p3)
ql_phim.them_phim(p4)
ql_phim.hien_thi()
ql_phim.xoa_phim("Avatar")
ql_phim.hien_thi()
