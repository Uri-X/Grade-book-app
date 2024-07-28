#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            return 0.0
        total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
        total_credits = sum(course['credits'] for course in self.courses_registered)
        self.GPA = total_points / total_credits
        return self.GPA

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})
