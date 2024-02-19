from visitor import AverageGradeVisitor
class Teacher:
    def __init__(self, name, id):
        """
        Initializes a new Teacher object with the given name and ID.

        Args:
        - name (str): The name of the teacher.
        - id (int): The ID of the teacher.
        """
        self.name = name
        self.id = id

    def __str__(self):
        """
        Returns a string representation of the Teacher object.

        Returns:
        - str: A string containing the name and ID of the teacher.
        """
        return f"Teacher: {self.name}, ID: {self.id}"

    def calculate_average_grade(self, student):
        """
        Calculates the average grade of a student by accepting a visitor object.

        Args:
        - student (Student): The student object for which the average grade is to be calculated.
        """
        visitor = AverageGradeVisitor()  # Create an instance of the AverageGradeVisitor
        student.accept(visitor)  # Make the student accept the visitor for calculating average grade