from student import Student
from teacher import Teacher

if __name__ == "__main__":
    # Create a teacher object
    teacher = Teacher("Dr. Smith", 1001)

    # Create student1 object and add grades
    student1 = Student("Alice", 1)
    student1.add_grade(90, 0.2)
    student1.add_grade(85, 0.2)
    student1.add_grade(95, 0.3)
    student1.add_grade(80, 0.3)
    student1.print_grades()  # Print student1's grades

    # Create student2 object and add grades
    student2 = Student("Bob", 2)
    student2.add_grade(75, 0.2)
    student2.add_grade(80, 0.2)
    student2.add_grade(85, 0.3)
    student2.add_grade(90, 0.3)
    student2.print_grades()  # Print student2's grades

    # Calculate and print the average grade for student1 and student2
    teacher.calculate_average_grade(student1)
    teacher.calculate_average_grade(student2)