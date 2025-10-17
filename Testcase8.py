# class Student:
class Student:

    # def ...(self, ...):
    def __init__(self, name):
        self.name = name
        self.grades = []

    # def add_grade(self, ...):
    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."   # return ...

    # def get_average(self):
    def get_average(self):
        avg = sum(self.grades) / len(self.grades)
        return f"Average grade: {avg:.1f}"   # return ...

# Test
student = Student("Alice")
print(student.add_grade(90))
print(student.add_grade(80))
print(student.add_grade(70))
print(student.get_average())
