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
