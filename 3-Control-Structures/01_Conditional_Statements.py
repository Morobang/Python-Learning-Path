# -------------------------------------------
# 📘 Python Conditional Statements Tutorial
# -------------------------------------------

# Conditional statements allow your code to make decisions based on logic.
# Main types: if, elif, else

# -------------------------------------------
# 🧠 Basic If Statement
# -------------------------------------------

age = 20

if age >= 18:
    print("You are an adult.")

# -------------------------------------------
# 🔁 If-Else Statement
# -------------------------------------------

if age < 18:
    print("You are a minor.")
else:
    print("You are 18 or older.")

# -------------------------------------------
# 🔄 If-Elif-Else Chain
# -------------------------------------------

grade = 75

if grade >= 90:
    print("Grade: A")
elif grade >= 75:
    print("Grade: B")
elif grade >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# -------------------------------------------
# 🧪 Comparison Operators
# -------------------------------------------
# ==   Equal
# !=   Not equal
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to

# -------------------------------------------
# ✅ Logical Operators
# -------------------------------------------
# and     Both conditions must be true
# or      At least one condition must be true
# not     Reverses a condition

# Example with logical operators
temperature = 30
is_sunny = True

if temperature > 25 and is_sunny:
    print("Great day for a picnic!")

# -------------------------------------------
# 🔁 Nested If Statements
# -------------------------------------------

logged_in = True
user_role = "admin"

if logged_in:
    if user_role == "admin":
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in.")

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ Use if/elif/else to control logic
# ✅ Use comparison and logical operators
# ✅ Combine conditions for more complex logic
# ✅ Use indentation correctly (very important in Python!)
