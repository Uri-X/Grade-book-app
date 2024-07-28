#!/usr/bin/python3
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

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_ranking(self):
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        for idx, student in enumerate(self.student_list, start=1):
            print(f"{idx}. {student.names} - GPA: {student.GPA}")

    def search_by_grade(self, grade_range):
        result = []
        for student in self.student_list:
            for course in student.courses_registered:
                if grade_range[0] <= course['grade'] <= grade_range[1]:
                    result.append(student)
                    break
        return result

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}:")
            for course in student.courses_registered:
                print(f"{course['course'].name} - Grade: {course['grade']}")
            print(f"GPA: {student.GPA}")
