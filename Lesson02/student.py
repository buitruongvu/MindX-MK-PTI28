class Student:
  def __init__(self, name, age, gender, school):
    self.name = name
    self.age = age
    self.gender = gender
    self.school = school
  def show(self):
    print("Name = ", self.name)
    print("Age = ", self.age)
    print("Gender = ", self.gender)
    print("School = ", self.school)