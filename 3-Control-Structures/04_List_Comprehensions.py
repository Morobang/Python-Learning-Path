# -------------------------------------------
# 🧾 Python List Comprehensions
# -------------------------------------------

# List comprehensions offer a shorter way to create lists.

# Basic structure:
# new_list = [expression for item in iterable if condition]

# -------------------------------------------
# 🔁 Example 1 – Basic For Loop vs List Comprehension
# -------------------------------------------

# Using a for loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("Squares (loop):", squares)

# Using list comprehension
squares_lc = [i ** 2 for i in range(1, 6)]
print("Squares (list comp):", squares_lc)

# -------------------------------------------
# 🧠 Example 2 – Add a condition
# -------------------------------------------

# Get even numbers from 1 to 10
evens = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", evens)

# -------------------------------------------
# 📝 Example 3 – Convert to uppercase
# -------------------------------------------

names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
print("Uppercase names:", upper_names)

# -------------------------------------------
# 🧮 Example 4 – With nested loops
# -------------------------------------------

# Create a list of (x, y) pairs for x and y in 1–3
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print("Coordinate pairs:", pairs)

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ List comprehensions make code cleaner and shorter
# ✅ You can add conditions (if)
# ✅ You can nest loops
# ✅ Always choose readability over cleverness
