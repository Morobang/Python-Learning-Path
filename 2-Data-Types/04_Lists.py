# ---------------------------------------
# 📘 Python List Data Type Tutorial
# ---------------------------------------

# A list is an ordered, mutable collection of items.
# Lists can store multiple values of any data type.

# ---------------------------------------
# 🧱 Creating Lists
# ---------------------------------------

fruits = ["apple", "banana", "mango", "orange"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "Python", True, 3.14]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed List:", mixed)

# ---------------------------------------
# 🔍 Accessing Elements
# ---------------------------------------

print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice (0:2):", fruits[0:2])

# ---------------------------------------
# 🛠️ Modifying Lists
# ---------------------------------------

fruits[1] = "grape"
print("\nModified Fruits:", fruits)

# ---------------------------------------
# ➕ Adding Items
# ---------------------------------------

fruits.append("kiwi")
print("After append:", fruits)

fruits.insert(1, "pear")
print("After insert at index 1:", fruits)

# ---------------------------------------
# ➖ Removing Items
# ---------------------------------------

fruits.remove("mango")
print("\nAfter remove:", fruits)

last_item = fruits.pop()
print("Popped item:", last_item)
print("After pop:", fruits)

# ---------------------------------------
# 📌 List Functions and Methods
# ---------------------------------------

print("\nLength of fruits:", len(fruits))
print("Is 'apple' in fruits?", "apple" in fruits)

numbers.sort()
print("Sorted numbers:", numbers)

numbers.reverse()
print("Reversed numbers:", numbers)

# ---------------------------------------
# 🔁 Looping Through Lists
# ---------------------------------------

print("\nLooping through fruits:")
for fruit in fruits:
    print("-", fruit)

# ---------------------------------------
# 🧪 List Comprehension (Advanced)
# ---------------------------------------

squares = [x**2 for x in range(1, 6)]
print("\nSquares using list comprehension:", squares)

# ---------------------------------------
# 🧠 Summary
# ---------------------------------------
# ✅ Lists are ordered and mutable
# ✅ Support indexing, slicing, and looping
# ✅ Use methods like append(), insert(), remove(), sort(), pop()
# ✅ List comprehension = powerful shortcut for creating lists
