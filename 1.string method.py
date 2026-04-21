course = "Python for Beginners"
print(course[4])
print(course[0:6])
print(course[1:-2])         # everything will be print except 1st letter and last 2 letter
print(len(course))
print(course.upper())
print(course.lower())
print(course.capitalize())          #Every word first letter print as capital
print(course.find('y'))
print(course.find('Python'))        #giving the starting index of the first letter
print(course.replace('y','ee'))
print('Python' in course)