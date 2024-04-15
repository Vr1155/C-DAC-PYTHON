# Question 1:

x = """
    Hello! This is the output of solutions.py
    and this message is 
    present in three different lines!
"""

print(x)

# Question 2:

def get_and_display_details():
    studentid = input("Enter student id: ")
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    university = input("Enter university: ")
    print("Here are the details: ")
    print(studentid, name, branch, university)

get_and_display_details()

# Question 3:

import solution3 as s

# a.)
a = s.area_of_rectangle(5,2)
b = s.area_of_square(5)

print("Area of rectangle: ", a, "Area of square:", b)


# b.) 
d = s.area_of_square(25)
print("Area of square: ", d)

# c.) 
e = s.area_of_rectangle(325, 20)
print("Area of rectangle: ", e)