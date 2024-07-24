#!/usr/bin/python3

class Course:
    """
    Represents a course with a name, trimester, and number of credits.
    """
    def __init__(self, name, trimester, credits):
        """
        Initializes a Course object.
        
        Args:
        name (str): The name of the course.
        trimester (str): The trimester in which the course is offered.
        credits (int): The number of credits for the course.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits

class Student:
    """
    Represents a student with an email, name, registered courses, and GPA.
    """
    def __init__(self, email, name):
        """
        Initializes a Student object.
        
        Args:
        email (str): The email of the student.
        name (str): The name of the student.
        """
        self.email = email
        self.name = name
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        """
        Calculates the GPA of the student based on registered courses.
        """
        total_credits = sum(course['course'].credits for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.0
            return

        total_points = sum(course['grade'] * course['course'].credits for course in self.courses_registered)
        self.GPA = total_points / total_credits

    def register_for_course(self, course, grade):
        """
        Registers the student for a course with a given grade.
        
        Args:
        course (Course): The course to register for.
        grade (float): The grade received in the course.
        """
        self.courses_registered.append({'course': course, 'grade': grade})
        self.calculate_GPA()

class GradeBook:
    """
    Manages student records, course records, and performs operations like registration, GPA calculation, and ranking.
    """
    def __init__(self):
        """
        Initializes a GradeBook object with empty student and course lists.
        """
        self.student_list = []
        self.course_list = []

    def add_student(self, email, name):
        """
        Adds a student to the GradeBook.
        
        Args:
        email (str): The student's email.
        name (str): The student's name.
        """
        student = Student(email, name)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        """
        Adds a course to the GradeBook.
        
        Args:
        name (str): The name of the course.
        trimester (str): The trimester in which the course is offered.
        credits (int): The number of credits for the course.
        """
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, email, course_name, grade):
        """
        Registers a student for a course.
        
        Args:
        email (str): The student's email.
        course_name (str): The name of the course.
        grade (float): The grade received in the course.
        """
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_GPA(self):
        """
        Calculates the GPA for all students.
        """
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        """
        Ranks students by GPA in descending order.
        
        Returns:
        list: Sorted list of students by GPA.
        """
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, min_grade, max_grade):
        """
        Searches for students within a specified grade range.
        
        Args:
        min_grade (float): Minimum GPA to search for.
        max_grade (float): Maximum GPA to search for.
        
        Returns:
        list: List of students within the specified GPA range.
        """
        return [s for s in self.student_list if min_grade <= s.GPA <= max_grade]

    def generate_transcript(self, email):
        """
        Generates a transcript for a student.
        
        Args:
        email (str): The student's email.
        
        Returns:
        str: Transcript of the student's courses and GPA.
        """
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            transcript = f"Transcript for {student.name} ({student.email}):\n"
            for registered in student.courses_registered:
                transcript += f"- {registered['course'].name}: Grade {registered['grade']}\n"
            transcript += f"GPA: {student.GPA:.2f}"
            return transcript
        return "Student not found."

def main():
    """
    Main function to interact with the GradeBook application.
    """
    grade_book = GradeBook()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Choose an action (1-8): ")
        
        if choice == "1":
            email = input("Enter student email: ")
            name = input("Enter student name: ")
            grade_book.add_student(email, name)
        
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            grade_book.add_course(name, trimester, credits)
        
        elif choice == "3":
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            grade_book.register_student_for_course(email, course_name, grade)
        
        elif choice == "4":
            grade_book.calculate_GPA()
            print("GPA calculated for all students.")
        
        elif choice == "5":
            ranked_students = grade_book.calculate_ranking()
            print("Student Rankings:")
            for student in ranked_students:
                print(f"{student.name} ({student.email}): GPA {student.GPA:.2f}")
        
        elif choice == "6":
            min_grade = float(input("Enter minimum GPA: "))
            max_grade = float(input("Enter maximum GPA: "))
            students = grade_book.search_by_grade(min_grade, max_grade)
            print("Students in the specified grade range:")
            for student in students:
                print(f"{student.name} ({student.email}): GPA {student.GPA:.2f}")
        
        elif choice == "7":
            email = input("Enter student email: ")
            transcript = grade_book.generate_transcript(email)
            print(transcript)
        
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
