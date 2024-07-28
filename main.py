#!/usr/bin/python3
def main():
    gradebook = GradeBook()
    while True:
        print("Choose an action:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for a course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("7. Exit")
        choice = input("Enter your choice: ")

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
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(email, course_name, grade)
        elif choice == '4':
            gradebook.calculate_ranking()
        elif choice == '5':
            lower_bound = float(input("Enter lower bound of grade range: "))
            upper_bound = float(input("Enter upper bound of grade range: "))
            students = gradebook.search_by_grade((lower_bound, upper_bound))
            for student in students:
                print(student.names)
        elif choice == '6':
            email = input("Enter student email: ")
            gradebook.generate_transcript(email)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
