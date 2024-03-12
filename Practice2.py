
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course, mark):
        self.marks[course] = mark

    def list_marks(self):
        for course, mark in self.marks.items():
            print(f"{course}: {mark}")


student1 = Student(1, "Alice", "2000-01-01")
student1.input_marks("Math", 85)
student1.input_marks("Science", 90)
student1.list_marks()

