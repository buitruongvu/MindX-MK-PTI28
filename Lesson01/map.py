#map(function, iterable)
# Ví dụ 1: Giả sử bạn có một danh sách giá tiền bằng USD. Bạn muốn quy đổi toàn bộ danh sách này sang tiền VNĐ (với tỷ giá 1 USD = 25.000 VNĐ).
#Cách 1: Dùng def thông thường
usd_prices = [10, 20, 50, 100]
#1. Tạo hàm xử lý
def convert_to_vnd(usd):
  return usd * 26000
#2. Đưa vào map()
vnd_prices = map(convert_to_vnd, usd_prices)
#3. Ép thành kiểu list để in ra
print(list(vnd_prices))
# cách 2: Dùng hàm ẩn danh lambda
usd_prices = [10, 20, 50, 100]
vnd_prices = map(lambda usd: usd * 26000, usd_prices)
print(list(vnd_prices))

#Ví dụ 2: Giả sử bạn có danh sách học sinh, và bạn chỉ muốn trích xuất ra một danh sách chứa toàn bộ Tên của các học sinh đó.
students = [
    {'id': 'HS01', 'name': 'Gia bảo', 'age': 11},
    {'id': 'HS02', 'name': 'Gia Khánh', 'age': 11},
    {'id': 'HS03', 'name': 'Bảo Nam', 'age': 14},
    {'id': 'HS04', 'name': 'Minh Đức', 'age': 12}
]

danh_sach_ten = list(map(lambda student: student["name"], students))
print("danh sách chỉ chứa tên:", danh_sach_ten)