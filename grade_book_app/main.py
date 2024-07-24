#!/usr/bin/python3

class Student:
    def __init__(self, name):
        self.name = name
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            total_credits = sum(course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})
        self.calculate_GPA()

    def __str__(self):
        return f"{self.name} (GPA: {self.GPA:.2f})"

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.credits} credits, {self.trimester})"

class GradeBook:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self):
        name = input("Enter the name of the student: ")
        student = Student(name)
        self.students.append(student)
        print(f"Student '{name}' added.")

    def add_course(self):
        name = input("Enter the name of the course: ")
        trimester = input("Enter the trimester: ")
        credits = int(input("Enter the number of credits: "))
        course = Course(name, trimester, credits)
        self.courses.append(course)
        print(f"Course '{name}' added.")

    def register_student_for_course(self):
        student_name = input("Enter the name of the student: ")
        course_name = input("Enter the name of the course: ")
        grade = float(input("Enter the grade: "))

        student = next((s for s in self.students if s.name == student_name), None)
        course = next((c for c in self.courses if c.name == course_name), None)

        if student and course:
            student.register_for_course(course, grade)
            print(f"Student '{student_name}' registered for course '{course_name}' with grade {grade}.")
        else:
            print("Student or course not found.")

    def calculate_GPA(self):
        for student in self.students:
            student.calculate_GPA()
        print("GPA calculated for all students.")

    def calculate_ranking(self):
        ranked_students = sorted(self.students, key=lambda s: s.GPA, reverse=True)
        print("Ranking of students based on GPA:")
        for i, student in enumerate(ranked_students, start=1):
            print(f"{i}. {student}")
        return ranked_students

    def search_by_grade(self):
        min_grade = float(input("Enter the minimum grade: "))
        max_grade = float(input("Enter the maximum grade: "))
        filtered_students = [s for s in self.students if any(min_grade <= course['grade'] <= max_grade for course in s.courses_registered)]
        print("Students with grades in the specified range:")
        for student in filtered_students:
            print(student)
        return filtered_students

    def generate_transcript(self):
        student_name = input("Enter the name of the student: ")
        student = next((s for s in self.students if s.name == student_name), None)

        if student:
            print(f"Transcript for {student_name}:")
            for course in student.courses_registered:
                print(f"{course['course']} - Grade: {course['grade']}, Credits: {course['credits']}")
            print(f"GPA: {student.GPA:.2f}")
            return student
        else:
            print("Student not found.")
            return None

def main():
    """
    Main function to run the GradeBook application.
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

        if choice == '1':
            grade_book.add_student()
        elif choice == '2':
            grade_book.add_course()
        elif choice == '3':
            grade_book.register_student_for_course()
        elif choice == '4':
            grade_book.calculate_GPA()
        elif choice == '5':
            grade_book.calculate_ranking()
        elif choice == '6':
            grade_book.search_by_grade()
        elif choice == '7':
            grade_book.generate_transcript()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()

