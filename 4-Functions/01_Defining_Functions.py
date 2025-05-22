# -------------------------------------------
# 🧩 Python Functions – Introduction
# -------------------------------------------

# A function is a block of reusable code that performs a specific task.
# Use functions to keep your code organized and avoid repetition.

# -------------------------------------------
# 🛠️ Defining a Function
# -------------------------------------------

def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()

# -------------------------------------------
# 📦 Function with Parameters
# -------------------------------------------

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Tshigidimisa")

# -------------------------------------------
# 🔁 Function with Return Value
# -------------------------------------------

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# -------------------------------------------
# 🧠 Multiple Parameters
# -------------------------------------------

def full_name(first, last):
    return f"{first} {last}"

print("Full Name:", full_name("Tshigidimisa", "Morobang"))

# -------------------------------------------
# 🎯 Default Parameters
# -------------------------------------------

def greet_with_message(name, message="Welcome!"):
    print(f"{message}, {name}!")

greet_with_message("Neo")
greet_with_message("Thabo", "Good to see you")

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ Use `def` to define a function
# ✅ Call functions using parentheses: `function_name()`
# ✅ Pass values using parameters
# ✅ Return results using `return`
# ✅ Use default parameters to make arguments optional
