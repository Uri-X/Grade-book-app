# test_gradebook.py

from database import (
    initialize_db, add_student, get_students, update_student_email, delete_student,
    add_course, enroll_student, get_enrollments
)

def test_database():
    # Initialize the database and tables
    initialize_db()
    
    # Add students
    print("Adding students...")
    add_student('John Doe', 'john.doe@example.com')
    add_student('Jane Smith', 'jane.smith@example.com')

    # Add courses
    print("Adding courses...")
    add_course('Mathematics')
    add_course('Science')
    
    # Enroll students in courses
    print("Enrolling students...")
    enroll_student(1, 1, 85.5)  # John Doe in Mathematics
    enroll_student(2, 2, 90.0)  # Jane Smith in Science
    
    # Fetch and display students
    print("\nStudents:")
    students = get_students()
    for student in students:
        print(student)
    
    # Fetch and display enrollments
    print("\nEnrollments:")
    enrollments = get_enrollments()
    for enrollment in enrollments:
        print(enrollment)
    
    # Update a student's email
    print("\nUpdating student email...")
    update_student_email(1, 'john.newemail@example.com')
    
    # Fetch and display students again
    print("\nUpdated Students:")
    students = get_students()
    for student in students:
        print(student)
    
    # Delete a student
    print("\nDeleting student...")
    delete_student(2)
    
    # Fetch and display students again
    print("\nFinal Students List:")
    students = get_students()
    for student in students:
        print(student)

# Run the test
if __name__ == "__main__":
    test_database()
