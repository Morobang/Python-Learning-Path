# -------------------------------------------
# 🧾 Function Arguments in Python
# -------------------------------------------

# Python supports several types of function arguments:
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Arbitrary arguments (*args and **kwargs)

# -------------------------------------------
# 1️⃣ Positional Arguments
# -------------------------------------------

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Tshigidimisa", 25)  # Order matters!

# -------------------------------------------
# 2️⃣ Keyword Arguments
# -------------------------------------------

greet(age=22, name="Morobang")  # Order doesn't matter

# -------------------------------------------
# 3️⃣ Default Arguments
# -------------------------------------------

def greet_user(name, country="South Africa"):
    print(f"{name} is from {country}.")

greet_user("Tshigi")                   # Uses default
greet_user("Tshigi", "Botswana")       # Overrides default

# -------------------------------------------
# 4️⃣ *args – Arbitrary Positional Arguments
# -------------------------------------------

def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Total sum: {total}")

add_numbers(5, 10)
add_numbers(1, 2, 3, 4, 5)

# -------------------------------------------
# 5️⃣ **kwargs – Arbitrary Keyword Arguments
# -------------------------------------------

def print_info(**person):
    for key, value in person.items():
        print(f"{key}: {value}")

print_info(name="Morobang", role="Data Analyst", level="Intern")

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ Positional – values passed in order
# ✅ Keyword – specify argument names
# ✅ Default – provide fallback values
# ✅ *args – accept many positional args as a tuple
# ✅ **kwargs – accept many keyword args as a dictionary
