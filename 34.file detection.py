import os

file_path = "test.txt"
if os.path.exists(file_path):
    print(f"File exist")
else:
    print("File not exist")

print(os.path.isfile(file_path))    #for check the file
print(os.path.isdir(file_path))     # for check the dir