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
