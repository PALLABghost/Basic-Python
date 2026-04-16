#instance method = best for the operation of the class(object)
                    #for accessing instance method we need create object like employee1 and
                    #then only we can access the data means constructor like name and position which is belongs
                    #that class

#static method = Best use for utility function that do not need class data like name and position.
                #a method that belongs to class , rather than any object from that class
                # like no need to create object like employee1

class Employee:
    def __init__(self, name,position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["cook","manager","cashier"]
        return position in valid_position

employee1 = Employee("Patrick", "manager")
employee2 = Employee("Spongebob", "cook")
print(Employee.is_valid_position("Rocket scientist"))
print(employee1.get_info())
print(employee2.get_info())
