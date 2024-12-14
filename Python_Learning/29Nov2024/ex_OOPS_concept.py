class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def student_info(self):
        sum1 = 0
        for val in self.marks:
            sum1 = sum1 + val
        print("student name is",self.name, "and average is", sum1/3)

s1 = Student("abhishek", [90, 80, 70])
# s2 = Student("Karan", 80)
# s3 = Student("Arjun", 70)
s1.student_info()