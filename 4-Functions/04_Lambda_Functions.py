# -------------------------------------------
# ⚡ Lambda Functions in Python
# -------------------------------------------

# A lambda function is a small anonymous function.
# Syntax: lambda arguments: expression

# -------------------------------------------
# 1️⃣ Basic Lambda Example
# -------------------------------------------

# Regular function
def square(x):
    return x * x

# Lambda version
square_lambda = lambda x: x * x

print("Regular:", square(5))
print("Lambda:", square_lambda(5))

# -------------------------------------------
# 2️⃣ Lambda with Multiple Arguments
# -------------------------------------------

add = lambda a, b: a + b
print("Add:", add(3, 7))

# -------------------------------------------
# 3️⃣ Lambda in Built-in Functions
# -------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Using lambda with map to square numbers
squared = list(map(lambda x: x ** 2, numbers))
print("Squared List:", squared)

# Using lambda with filter to get even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even)

# -------------------------------------------
# 4️⃣ Lambda as One-Liner Functions
# -------------------------------------------

# Good for quick, simple tasks
greet = lambda name: f"Hello, {name}!"
print(greet("Tshigidimisa"))

# -------------------------------------------
# ⚠️ When NOT to Use Lambda
# -------------------------------------------
# 🔸 Avoid for complex logic or multiple lines
# 🔸 Use regular `def` functions for readability

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ Lambda = quick one-line function
# ✅ Syntax: lambda args: expression
# ✅ Great with functions like map(), filter(), and sorted()
