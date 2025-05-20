# ---------------------------------------
# 📘 Python Tuple Data Type Tutorial
# ---------------------------------------

# A tuple is an ordered, immutable collection of items.
# Once created, you cannot modify a tuple (unlike lists).

# ---------------------------------------
# 🧱 Creating Tuples
# ---------------------------------------

# With parentheses
person = ("Tshigidimisa", 24, "Data Analyst")

# Without parentheses (optional, but recommended to use them)
coordinates = 34.05, -118.25

# Single-element tuple (must include a trailing comma)
single_item = ("Python",)

print("Person Tuple:", person)
print("Coordinates Tuple:", coordinates)
print("Single Item Tuple:", single_item)

# ---------------------------------------
# 🔍 Accessing Tuple Elements
# ---------------------------------------

print("\nName:", person[0])
print("Age:", person[1])
print("City (from coordinates):", coordinates[0])

# ---------------------------------------
# 🔁 Looping Through a Tuple
# ---------------------------------------

print("\nLooping through 'person':")
for item in person:
    print("-", item)

# ---------------------------------------
# 🛑 Immutability Example
# ---------------------------------------

# person[1] = 25  # ❌ This would raise a TypeError

# ---------------------------------------
# ✅ Tuple Methods
# ---------------------------------------

numbers = (1, 2, 3, 2, 4, 2)

print("\nCount of 2:", numbers.count(2))
print("Index of 4:", numbers.index(4))

# ---------------------------------------
# 🔄 Tuple vs List
# ---------------------------------------

# Tuple = Immutable, faster, used when data shouldn't change
# List  = Mutable, more flexible, used when data might change

example_list = [1, 2, 3]
example_tuple = (1, 2, 3)

print("\nList:", example_list)
print("Tuple:", example_tuple)

# ---------------------------------------
# 🧠 Summary
# ---------------------------------------
# ✅ Tuples are ordered, immutable
# ✅ Use () to define; commas matter
# ✅ Useful for fixed data, coordinates, and safe data grouping
