class Student:
  name = "Bùi Trường Vũ"
  age = 24
  gender = "Male"
  school = "Mindx Technology School"

# Để truy cập thuộc tính của đối tượng ta dùng cách viết sau
# <Đối tượng>.<Thuộc tính>
# <Tên đối tượng> = <Tên lớp>()
st1 = Student()
ten = st1.name
print(ten)
# Cách thay đổi thuộc tính của đối tượng bằng cách gán trực tiếp
# <Đối tượng>.<Thuộc tính> = <Giá trị mới>
st1.name = "Du Gia Bao"
print(st1.name)

#