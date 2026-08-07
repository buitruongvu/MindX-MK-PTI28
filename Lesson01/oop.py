# Tư duy OOP - Thế giới thực trong Code 
# Khái niệm cốt lõi:
# Class (Bản thiết kế): Ví dụ như bản vẽ của một chiếc ô tô, hay khuôn làm bánh.
# Object (Thực thể): Chiếc ô tô Vinfast thật chạy ngoài đường, hay những chiếc bánh biskit nướng ra từ khuôn.
# Đặc điểm:
# Attribute (Thuộc tính - Danh từ/Tính từ): Đặc điểm nhận dạng (tên, tuổi, giới tính...).
# Method (Phương thức - Động từ): Hành động đối tượng có thể làm (hát, hiển thị thông tin...).

class Human:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def __str__(self):
    return f"Name: {self.name}, age: {self.age}, gender: {self.gender}"
  def sing(self, song_name):
    print(f"{self.name} sing {song_name}")


human1 = Human("Phuc Nguyen", 13, "male")
human2 = Human("Bao Lam", 13, "male")
print(human1)
human2.sing("Happy birthday!!")

    