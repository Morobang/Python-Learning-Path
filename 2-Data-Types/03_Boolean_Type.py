# ---------------------------------------
# 📘 Python Boolean Data Type Tutorial
# ---------------------------------------

# Boolean values represent one of two states: True or False
# Used in decision-making, comparisons, and control flow

# ---------------------------------------
# ✅ Boolean Values
# ---------------------------------------

is_python_fun = True
is_sky_green = False

print("Is Python fun?", is_python_fun)
print("Is the sky green?", is_sky_green)

print("Type of is_python_fun:", type(is_python_fun))

# ---------------------------------------
# 🔍 Boolean from Comparisons
# ---------------------------------------

print("\n10 > 5:", 10 > 5)
print("3 == 3:", 3 == 3)
print("7 != 2:", 7 != 2)
print("4 < 2:", 4 < 2)

# ---------------------------------------
# 🧮 Boolean with Logical Operators
# ---------------------------------------

a = 5
b = 10

# and → True if both are True
print("\n(a > 0 and b > 0):", a > 0 and b > 0)

# or → True if at least one is True
print("(a > 0 or b < 0):", a > 0 or b < 0)

# not → Reverses the result
print("not(a == 5):", not(a == 5))

# ---------------------------------------
# 🎯 Boolean in Conditionals
# ---------------------------------------

age = 18

if age >= 18:
    print("\nYou are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ---------------------------------------
# 📌 Truthy and Falsy Values
# ---------------------------------------

print("\nbool(1):", bool(1))        # True
print("bool(0):", bool(0))        # False
print("bool('Python'):", bool("Python"))  # True
print("bool(''):", bool(""))      # False
print("bool([]):", bool([]))      # False (empty list)
print("bool([1, 2]):", bool([1, 2]))  # True

# ---------------------------------------
# 🧠 Summary
# ---------------------------------------
# ✅ Booleans: True / False
# ✅ Generated from comparisons
# ✅ Used in if-else statements
# ✅ Logical operators: and, or, not
# ✅ Truthy and Falsy values help control program flow
