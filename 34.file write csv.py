import csv
file_path = "Employee.csv"
employee = [["Name","Age","Job"],
            ["Bob", 21, "Cook"],
            ["Josh",26, "Manager"]]

with open(file_path,"w",newline="") as file:
    writer = csv.writer(file)   #it will create the csv file
    for row in employee:
        writer.writerow(row)
    print(f"CSV file has been created name as {file_path}")