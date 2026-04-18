class Student:
    class_year = 2024    # class variable ,shared among the all instances of a class
    num_of_student = 0                #define outside of the constractor
                        #allow the share data between all object created in the class

    def __init__(self,name,age):     #__init__(self) is a constractor
        self.name = name            #intance variable
        self.age = age
        Student.num_of_student += 1     #calling class variable and when a student(object) created increment the num

student1 = Student("Suresh", 30)  #object created in class
student2 = Student("Roma", 35)
student3 = Student("Jesh", 37)

print(student2.name)
print(student2.age)
print(Student.class_year)       # we can call the variable with created object also,
                                # for best practice its should called with Class, so we can identify as a class variable
print(f"My Graduating class of {Student.class_year} has {Student.num_of_student} students")

