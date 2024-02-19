We are using a visitor to calculate the total grade of a student given their past grades, a simple average, this was put in visitor.py. The teacher class can only use the visitor and calculate the average grade for any student, so the student is passed to the teacher, the visitor function is called by the teacher on the student. The student on the other hand has an attribute that _accepts_ the visitor.



## Student Class
### Methods

- `__str__(self)`: Returns a string representation of the Student object.
- `add_grade(self, grade, weight)`: Adds a grade to the student's record.
- `accept(self, visitor)`: Accepts a visitor object and triggers the visitation on the student.
- `print_grades(self)`: prints all grades added for the student

## Teacher Class
### Methods

- `__str__(self)`: Returns a string representation of the Teacher object.
- `calculate_average_grade(self, student)`: Calculates the average grade of a student by accepting a visitor object.


## Visitor Class
### Methods

#### `visit_student(self, student)`
A method intended for subclasses to implement specific actions on a `Student` object.

## AverageGradeVisitor Class
### Methods

#### `visit_student(self, student)`
Calculates and prints the average grade of a `Student` object.