# ---------------------------------------
# 📘 Python Set Data Type Tutorial
# ---------------------------------------

# A set is an unordered, mutable collection of unique elements.
# Sets are useful for removing duplicates and performing set operations.

# ---------------------------------------
# 🧱 Creating Sets
# ---------------------------------------

fruits = {"apple", "banana", "orange", "apple"}
numbers = set([1, 2, 3, 3, 4, 5])

print("Fruits set (no duplicates):", fruits)
print("Numbers set:", numbers)

# ---------------------------------------
# ➕ Adding Elements
# ---------------------------------------

fruits.add("kiwi")
print("\nAfter adding 'kiwi':", fruits)

# ---------------------------------------
# ➖ Removing Elements
# ---------------------------------------

fruits.remove("banana")  # Raises error if not found
fruits.discard("grape")  # Safe: won't raise error if not found
print("After removing 'banana' and discarding 'grape':", fruits)

# ---------------------------------------
# 🔁 Looping Through a Set
# ---------------------------------------

print("\nLooping through fruits:")
for fruit in fruits:
    print("-", fruit)

# ---------------------------------------
# 📚 Set Operations
# ---------------------------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\nUnion (A | B):", set_a | set_b)
print("Intersection (A & B):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference (A ^ B):", set_a ^ set_b)

# ---------------------------------------
# ✅ Set Methods Summary
# ---------------------------------------
# add(), remove(), discard(), clear()
# union(), intersection(), difference(), symmetric_difference()

# ---------------------------------------
# ⚠️ Important Notes
# ---------------------------------------
# ❌ No indexing or slicing (unordered)
# ✅ Use sets to eliminate duplicates from lists

duplicates = [1, 2, 2, 3, 3, 4]
unique = set(duplicates)
print("\nUnique values from list:", unique)

# ---------------------------------------
# 🧠 Summary
# ---------------------------------------
# ✅ Sets are unordered, mutable, no duplicates
# ✅ Great for uniqueness and set math
# ✅ Fast membership testing (e.g., "in" keyword)
