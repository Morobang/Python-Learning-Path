# 03_Variables_and_Data_Types.py
"""
Variables and Data Types in Python

In Python, variables are used to store data.
You don't need to declare their type — Python infers it automatically.
"""

print(" Variables and Data Types")
print("-" * 40)

# String
name = "Tshigidimisa"
print(f"name (str): {name} — {type(name)}")

# Integer
age = 25
print(f"age (int): {age} — {type(age)}")

# Float
height = 1.75
print(f"height (float): {height} — {type(height)}")

# Boolean
is_student = True
print(f"is_student (bool): {is_student} — {type(is_student)}")

# List
skills = ["Python", "SQL", "Power BI"]
print(f"skills (list): {skills} — {type(skills)}")

# Tuple
coordinates = (10.5, 20.3)
print(f"coordinates (tuple): {coordinates} — {type(coordinates)}")

# Dictionary
profile = {"name": name, "age": age, "student": is_student}
print(f"profile (dict): {profile} — {type(profile)}")

# NoneType
nothing = None
print(f"nothing (NoneType): {nothing} — {type(nothing)}")

print("\n Python infers the type, but you can check with type()")
print(" Variable names should be descriptive and follow snake_case naming.")
