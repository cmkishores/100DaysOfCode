class School:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f"Name : {self.name} \n Age : {self.age} ")

class Student(School):
    def __init__(self, name, age, rollno):
        School.__init__(self, name, age)
        self.rollno = rollno
    def display_details(self):
         print(f"Student\nName : {self.name} \n Age : {self.age} \n RollNo : {self.rollno}")

class Teacher(School):
    def __init__(self, name, age, UID):
        School.__init__(self, name, age)
        self.UID = UID
    def display_details(self):
         print(f"Teacher\nName : {self.name} \n Age : {self.age} \n UID : {self.UID}")

S1 = Student("RandomStudent1",21,60)
s2 = Student("RandomStudent2",20,65)
t1 = Teacher("GoodTeacher1",26,"TCR2019")
S1.display_details()
s2.display_details()
t1.display_details()
