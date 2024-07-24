#!/usr/bin/python3
class GradeBook:
    """
    Manages student and course records, including adding students and courses,
    registering students for courses, calculating GPAs, and generating transcripts.
    """
    def __init__(self):
        """
        Initializes a GradeBook object with empty student and course lists.
        """
        self.student_list = []
        self.course_list = []

    def add_student(self):
        """
        Prompts the user to enter student details and adds a new Student
        object to the student_list.
        """
        email = input("Enter student email: ")
        names = input("Enter student name: ")
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self):
        """
        Prompts the user to enter course details and adds a new Course
        object to the course_list.
        """
        name = input("Enter course name: ")
        trimester = input("Enter trimester: ")
        credits = int(input("Enter credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self):
        """
        Prompts the user to register a student for a course and assigns a grade.
        
        Searches for the student and course in the respective lists and updates
        the student's courses_registered attribute with the given course and grade.
        """
        email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade: "))
        
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        
        if student and course:
            student.register_for_course(course, grade)
        else:
            print("Student or Course not found.")

    def calculate_GPA(self):
        """
        Calculates and updates the GPA for all students in the student_list.
        """
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        """
        Sorts the students by GPA in descending order and returns the sorted list.
        
        Returns:
        List of Student objects sorted by GPA.
        """
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        return self.student_list

    def search_by_grade(self):
        """
        Prompts the user for a GPA range and returns a list of students whose
        GPA falls within that range.
        
        Returns:
        List of Student objects with GPA within the specified range.
        """
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        results = [s for s in self.student_list if min_grade <= s.GPA <= max_grade]
        return results

    def generate_transcript(self):
        """
        Prompts the user for a student email and generates a transcript showing
        the student's GPA.
        
        Returns:
        A string containing the transcript information or a message if the student
        is not found.
        """
        email = input("Enter student email: ")
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            return f"Transcript for {student.names}: GPA = {student.GPA:.2f}"
        return "Student not found."
