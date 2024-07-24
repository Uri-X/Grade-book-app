class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0
        self.grades = {}  # Dictionary to store course grades

    def calculate_GPA(self):
        total_points = sum(course.credits for course in self.courses_registered)
        if total_points == 0:
            self.GPA = 0.0
        else:
            total_credits = sum(course.credits for course in self.courses_registered)
            total_grades = sum(self.grades[course.name] * course.credits for course in self.courses_registered)
            self.GPA = total_grades / total_credits

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def add_grade(self, course_name, grade):
        self.grades[course_name] = grade
course.py
python
Copy code
class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
