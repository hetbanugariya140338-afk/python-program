class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print(f"Roll No: {self.rollno}\nName: {self.name}\nGender: {self.gender}\nAge: {self.age}")

class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        # Initialize parent class attributes
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        self.display_student()
        print(f"Course: {self.coursename}\nDuration: {self.duration}\nFee: {self.fee}")

# Usage
obj = Course(101, "Alice", "Female", 20, "Computer Science", "4 Years", 50000)
obj.display_course()