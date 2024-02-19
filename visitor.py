class Visitor:
    def visit_student(self, student):
        pass

class AverageGradeVisitor(Visitor):
    def visit_student(self, student):
        total_grade = sum(student.grades)
        print(f"The average grade of {student.name} is: {total_grade:.2f}")
