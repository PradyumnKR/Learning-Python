import statistics

class Student:
    def __init__(self, name, rollno, grades=None):
        self.name = name 
        self.rollno = rollno 
        self.grades = grades if grades is not None else [] # Fixed the list bug

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)): # Checks for both int and float
            print("Invalid Data Type.")
            return
        if grade < 0:
            print("Negative Values not permitted.")
            return
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0 # Return 0 so math doesn't break later
        return statistics.mean(self.grades)
    
class School:
    def __init__(self, name):
        self.school_name = name 
        self.students = []

    def add_student(self, student_obj):
        if isinstance(student_obj, Student): # Professional type checking
            self.students.append(student_obj)
        else:
            print("Invalid Student Object.")

    def get_school_average(self):
        if not self.students:
            return 0
        total = sum(s.get_average() for s in self.students)
        return total / len(self.students)

# Testing the logic
school = School("Hogwarts")
s1 = Student("Harry", 1)
s1.add_grade(90)
s2 = Student("Ron", 2)
s2.add_grade(70)

school.add_student(s1)
school.add_student(s2)

print(f"{school.school_name} Average: {school.get_school_average()}")