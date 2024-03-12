
from domains.Student import Student
from output import display_student_info

student1 = Student(1, "Alice", "2000-01-01")
student1.input_marks("Math", 85)
student1.input_marks("Science", 90)
student1.list_marks()

credits = [3, 4]  
gpa = student1.calculate_gpa(credits)
print(f"Student GPA: {gpa}")


display_student_info(student1)
