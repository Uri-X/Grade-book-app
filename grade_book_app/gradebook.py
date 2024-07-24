from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name):
        student = self.find_student_by_email(student_email)
        course = self.find_course_by_name(course_name)
        if student and course:
            student.register_for_course(course)

    def calculate_GPA(self, student_email):
        student = self.find_student_by_email(student_email)
        if student:
            student.calculate_GPA()

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, grade):
        return [student for student in self.student_list if any(g == grade for g in student.grades.values())]

    def generate_transcript(self, student_email):
        student = self.find_student_by_email(student_email)
        if student:
            return {
                'email': student.email,
                'names': student.names,
                'GPA': student.GPA,
                'courses': [(course.name, student.grades.get(course.name, 'N/A')) for course in student.courses_registered]
            }

    def add_grade(self, student_email, course_name, grade):
        student = self.find_student_by_email(student_email)
        if student:
            student.add_grade(course_name, grade)

    def find_student_by_email(self, email):
        for student in self.student_list:
            if student.email == email:
                return student
        return None

    def find_course_by_name(self, name):
        for course in self.course_list:
            if course.name == name:
                return course
        return None
