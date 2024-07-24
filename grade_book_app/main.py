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
            print("GPA calculated for all students.")
        elif choice == '5':
            ranked_students = grade_book.calculate_ranking()
            for i, student in enumerate(ranked_students, start=1):
                print(f"{i}. {student.email} - GPA: {student.GPA:.2f}")
        elif choice == '6':
            students_by_grade = grade_book.search_by_grade()
            for student in students_by_grade:
                print(f"{student.email} - GPA: {student.GPA:.2f}")
        elif choice == '7':
            transcript = grade_book.generate_transcript()
            print(transcript)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
