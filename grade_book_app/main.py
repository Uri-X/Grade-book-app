from gradebook import GradeBook
from utils import save_gradebook, load_gradebook

def main():
    gradebook = load_gradebook()
    if not gradebook:
        gradebook = GradeBook()

    while True:
        print("Choose an action:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for a course")
        print("4. Add student grade")
        print("5. Calculate ranking")
        print("6. Search by grade")
        print("7. Generate transcript")
        print("8. Save and Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(student_email, course_name)
        elif choice == '4':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.add_grade(student_email, course_name, grade)
        elif choice == '5':
            ranking = gradebook.calculate_ranking()
            for idx, student in enumerate(ranking, start=1):
                print(f"{idx}. {student.names} - GPA: {student.GPA}")
        elif choice == '6':
            grade = float(input("Enter grade to search for: "))
            students = gradebook.search_by_grade(grade)
            for student in students:
                print(f"{student.names} - GPA: {student.GPA}")
        elif choice == '7':
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"Transcript for {transcript['names']} (Email: {transcript['email']})")
                print(f"GPA: {transcript['GPA']}")
                for course in transcript['courses']:
                    print(f"{course[0]}: {course[1]}")
        elif choice == '8':
            save_gradebook(gradebook)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
