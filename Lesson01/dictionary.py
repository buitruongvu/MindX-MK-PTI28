# Dictinary
# CRUD (Create - Read - Update - Delete)
# Create
student1 = {
  "name": "Du Gia Bao", #key: value
  "age": 11,
  "school": "THCS Thanh Tri"
}
print(f'bạn {student1["name"]} hiện đang {student1["age"]} tuổi')

# Tạo một list chứa các dictionary
students = [
    {
        'id': 'HS01',
        'name': 'Gia Khanh',
        'age': 11,
        'gender': 'male',
        'scores': {'toan': 9.0, 'python': 10.0}
    },
    {
        'id': 'HS02',
        'name': 'Minh Duc',
        'age': 12,
        'gender': 'male',
        'scores': {'toan': 8.5, 'python': 9.5}
    },
    {
        'id': 'HS03',
        'name': 'Bao Nam',
        'age': 14,
        'gender': 'male',
        'scores': {'toan': 7.0, 'python': 8.0}
    }
]
#Read
print("===DANH SACH HOC SINH======")
for student in students:
  name = student["name"]
  age = student["age"]
  python_score = student["scores"]["python"]
  print(f"Học sinh tên {name} {age} tuổi - có điểm Python: {python_score}")

# Update
for student in students:
  if student["id"] == "HS03":
    student['scores']['toan'] = 8.0
    print(f"Đã cập nhật thông tin cho học sinh {student["name"]} như sau {student}")

#Delete
student1 = {
  "id": "HS1",
  "name": "Du Gia Bao", #key: value
  "age": 11,
  "school": "THCS Thanh Tri"
}
del student1['school']
print(student1)

# Advanced
# Read
# Lấy tất cả key của một dictinary
student1_key = list(student1.keys())
print(student1_key)
print(list(student1.items()))

