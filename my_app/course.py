#!/usr/bin/python3
class Student:
    """
    Represents a student with an email, name, and registered courses.
    """
    def __init__(self, email, names):
        """
        Initializes a Student object.

        Args:
        email (str): The student's email address.
        names (str): The student's full name.
        """
        self.email = email
        self.names = names
        self.courses_registered = {}  # {Course: grade}
        self.GPA = 0.0

    def calculate_GPA(self):
        """
        Calculates the student's GPA based on registered courses and grades.
        Updates the student's GPA attribute.
        """
        if not self.courses_registered:
            self.GPA = 0.0
            return
        total_credits = 0
        weighted_sum = 0
        for course, grade in self.courses_registered.items():
            total_credits += course.credits
            weighted_sum += grade * course.credits
        self.GPA = weighted_sum / total_credits

    def register_for_course(self, course, grade):
        """
        Registers the student for a course with a given grade.

        Args:
        course (Course): The course to register for.
        grade (float): The grade received in the course.
        """
        self.courses_registered[course] = grade

class Course:
    """
    Represents a course with a name, trimester, and credits.
    """
    def __init__(self, name, trimester, credits):
        """
        Initializes a Course object.

        Args:
        name (str): The course name.
        trimester (str): The trimester in which the course is taken.
        credits (int): The number of credits for the course.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    """
    Represents a grade book that manages students and courses.
    """
    def __init__(self):
        """
        Initializes a GradeBook object.
        """
        self.students = []
        self.courses = []

    def add_student(self, email, names):
        """
        Adds a student to the grade book.

        Args:
        email (str): The student's email address.
        names (str): The student's full name.
        """
        student = Student(email, names)
        self.students.append(student)

    def add_course(self, name, trimester, credits):
        """
        Adds a course to the grade book.

        Args:
        name (str): The course name.
        trimester (str): The trimester in which the course is taken.
        credits (int): The number of credits for the course.
        """
        course = Course(name, trimester, credits)
        self.courses.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        """
        Registers a student for a course with a given grade.

        Args:
        student_email (str): The student's email address.
        course_name (str): The course name.
        grade (float): The grade received in the course.
        """
        student = next((s for s in self.students if s.email == student_email), None)
        course = next((c for c in self.courses if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_GPA_for_student(self, student_email):
        """
        Calculates the GPA for a specific student.

        Args:
        student_email (str): The student's email address.
        """
        student = next((s for s in self.students if s.email == student_email), None)
        if student:
            student.calculate_GPA()
            print(f"GPA for {student.names} ({student.email}) is {student.GPA:.2f}")
        else:
            print("Student not found.")
