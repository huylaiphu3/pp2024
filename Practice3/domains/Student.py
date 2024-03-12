import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course, mark):
        rounded_mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
        self.marks[course] = rounded_mark

    def list_marks(self):
        for course, mark in self.marks.items():
            print(f"{course}: {mark}")

    def calculate_gpa(self, credits):
        marks_array = np.array(list(self.marks.values()))
        credits_array = np.array(credits)
        weighted_sum = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)
        gpa = weighted_sum / total_credits
        return round(gpa, 2)


