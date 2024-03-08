'''
Assignment:
Create a class called Student with attributes name, age, and grades
(a list of grades). Implement methods to calculate the average grade
of the student and to add a new grade to the list.
'''
class Student:
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Added grade {grade} to {self.name}'s record.")

    def average_grade(self):
        if not self.grades:
            print("No grades available.")
            return None
        return sum(self.grades) / len(self.grades)

# Test the Student class
student1 = Student("Alice", 20, [85, 90, 95])
student1.add_grade(88)
print(f"{student1.name}'s average grade: {student1.average_grade()}")

student2 = Student("Bob", 21)
student2.add_grade(75)
student2.add_grade(80)
print(f"{student2.name}'s average grade: {student2.average_grade()}")
