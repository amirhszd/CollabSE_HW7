class Student:
    def __init__(self, name, id):
        """
        Initializes a new Student object with the given name and ID.

        Args:
        - name (str): The name of the student.
        - id (int): The ID of the student.
        """
        self.name = name
        self.id = id
        self.grades = []

    def __str__(self):
        """
        Returns a string representation of the Student object.

        Returns:
        - str: A string containing the name and ID of the student.
        """
        return f"Student: {self.name}, ID: {self.id}"

    def add_grade(self, grade, weight):
        self.grades.append(grade*weight)

    def print_grades(self):
        print(f"{self.name} grades:", self.grades)

    def accept(self, visitor):
        visitor.visit_student(self)
