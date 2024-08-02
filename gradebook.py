from database import initialize_db, add_student, add_course, register_student_for_course, get_students, get_courses, get_student_courses
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        initialize_db()

    def add_student(self, email, names):
        add_student(email, names)

    def add_course(self, name, trimester, credits):
        add_course(name, trimester, credits)

    def register_student_for_course(self, student_email, course_name, grade):
        courses = get_courses()
        course = next((c for c in courses if c[0] == course_name), None)
        if course:
            trimester = course[1]
            register_student_for_course(student_email, course_name, trimester, grade)

    def calculate_ranking(self):
        students = get_students()
        student_objects = []
        for student in students:
            student_obj = Student(student[0], student[1])
            courses = get_student_courses(student[0])
            for course in courses:
                student_obj.register_for_course(Course(course[0], course[1], course[2]), course[3])
            student_obj.calculate_GPA()
            student_objects.append(student_obj)
        student_objects.sort(key=lambda x: x.GPA, reverse=True)
        for idx, student in enumerate(student_objects, start=1):
            print(f"{idx}. {student.names} - GPA: {student.GPA}")

    def search_by_grade(self, grade_range):
        students = get_students()
        result = []
        for student in students:
            student_obj = Student(student[0], student[1])
            courses = get_student_courses(student[0])
            for course in courses:
                if grade_range[0] <= course[3] <= grade_range[1]:
                    result.append(student_obj)
                    break
        return result

    def generate_transcript(self, student_email):
        student = next((s for s in get_students() if s[0] == student_email), None)
        if student:
            student_obj = Student(student[0], student[1])
            courses = get_student_courses(student[0])
            for course in courses:
                student_obj.register_for_course(Course(course[0], course[1], course[2]), course[3])
            print(f"Transcript for {student_obj.names}:")
            for course in student_obj.courses_registered:
                print(f"{course['course'].name} - Grade: {course['grade']}")
            print(f"GPA: {student_obj.GPA}")

    def view_students(self):
        students = get_students()
        print("List of Students:")
        for student in students:
            print(f"Email: {student[0]}, Names: {student[1]}")
