# 02_Python_Syntax_and_Indentation.py
"""
Python Syntax and Indentation

Python uses indentation (whitespace) to define code blocks.
This is a core part of the language and must be used consistently.
"""

print(" Python Syntax and Indentation")
print("-" * 40)

print("\n Example 1: Correct indentation")
age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are underage.")
    print("You cannot vote yet.")

print("\n Example 2: Incorrect indentation (will raise an error if uncommented)")
# Uncomment the lines below to see a syntax error
# if age >= 18:
# print("This line is not indented correctly!")

print("\n Tip: Use 4 spaces per indentation level (don't mix tabs and spaces).")

# Bonus: A for loop example
print("\n Example 3: Loop with proper indentation")
for i in range(3):
    print(f"Loop count: {i}")
print("Loop finished.")
