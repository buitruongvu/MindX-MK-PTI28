class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
       
    def tinh_chu_vi(self):
        return (self.chieu_rong + self.chieu_dai)*2
   
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

hcn = HinhChuNhat(6, 5)
print(hcn.tinh_chu_vi()) # output: 22
print(hcn.tinh_dien_tich()) # output: 30
