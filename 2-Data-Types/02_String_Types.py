# ---------------------------------------
# 📘 Python String Data Type Tutorial
# ---------------------------------------

# A string is a sequence of characters enclosed in quotes
# You can use single (' '), double (" "), or triple (''' ''' / """ """) quotes

# ---------------------------------------
# 🧵 Creating Strings
# ---------------------------------------

first_name = 'Tshigidimisa'
last_name = "Morobang"
full_name = first_name + " " + last_name

print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)

# Multiline string
bio = """I am learning Python
to become a skilled data analyst and engineer."""
print("\nMultiline String:\n", bio)

# ---------------------------------------
# 🧮 String Operations
# ---------------------------------------

greeting = "Hello, World!"

# Length of string
print("\nLength of greeting:", len(greeting))

# Accessing characters
print("First character:", greeting[0])
print("Last character:", greeting[-1])

# Slicing
print("Slice (0:5):", greeting[0:5])
print("Slice (7:):", greeting[7:])

# Concatenation
language = "Python"
version = "3.12"
print("Using + :", language + " " + version)

# Repetition
print("Repeat:", "Hi! " * 3)

# ---------------------------------------
# 🔧 String Methods
# ---------------------------------------

message = "  learn python with tshigidimisa  "

print("\nOriginal message:", message)
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Title case:", message.title())
print("Stripped:", message.strip())
print("Replace:", message.replace("python", "data analysis"))

# ---------------------------------------
# 🔍 String Checks
# ---------------------------------------

print("\nIs alphabetic?", "Data".isalpha())
print("Is numeric?", "12345".isdigit())
print("Starts with 'learn'?", message.strip().startswith("learn"))
print("Ends with 'tshigidimisa'?", message.strip().endswith("tshigidimisa"))

# ---------------------------------------
# 📌 f-Strings (String Formatting)
# ---------------------------------------

age = 24
print(f"\nMy name is {full_name} and I am {age} years old.")
