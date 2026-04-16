#class method = best for class level data or require access to class itself

class Student:
    count = 0
    total_gpa =0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of student {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0 :
            return 0
        else:
            return f"Average GPA {cls.total_gpa/cls.count}"

student1 = Student("Patrik", 40)
student2 = Student("Ram", 78)
print(student1.get_info())
print(student2.get_info())
print(Student.get_count())
print(Student.get_average_gpa())