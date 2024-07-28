PROJECT BRIEF

The Grade Book Application is a Python program that allows users to create and manage student records, course records, and transcripts. It includes features for course registration, GPA calculation, and data structure search and ranking.

Objectives
Create student records using user input
Store student information, including email, names, and courses registered
Create course records with name, trimester, and credits
Allow students to register for courses
Calculate and save the GPA for each student
Provide a ranking of students based on their GPA
Search students by grade obtained in a course
Create transcripts for each student showing their GPA

REQUIREMENTS

Student Class
Attributes: email, names, courses_registered, GPA
Methods: calculate_GPA(), register_for_course()
Course Class
Attributes: name, trimester, credits
Methods: None
Grade Book Class
Attributes: student_list, course_list
Methods:
add_student()
add_course()
register_student_for_course()
calculate_GPA()
calculate_ranking()
search_by_grade()
generate_transcript()
User Interface
Prompt the user to choose an action (add student, add a course, register the student for a course, calculate the ranking, search by grade, generate transcript)
Gather necessary input from the user (student information, course information, grade range)
Display the results of the chosen action
