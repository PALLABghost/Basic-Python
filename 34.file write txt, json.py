import os
import json
text = "I like pizza"

file_path = "text.txt"

with open(file_path, "a") as file:  #w for created file if file exist also. x for create file but it will not work when file already exist
    file.write("\n" + text)
    print(f"file {file_path} was created")

students = ["Ram", "Sam", "Petter"]
file_path3 = "student.txt"
with open(file_path3, "w") as file:
    for student in students:
        file.write(student + " ")
    print("students are added")

file_path2 = "employee.json"
employee = {
        "name" : "Pallab kr basak",
        "age"   : "28"
}
with open (file_path2 , "w") as file:
    json.dump(employee,file, indent= 4)
    print("dictionary is created")




