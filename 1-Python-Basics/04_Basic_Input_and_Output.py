# 04_Basic_Input_and_Output.py
"""
Basic Input and Output in Python

Learn how to take input from the user and display output in Python using input() and print().
"""

print(" Basic Input and Output")
print("-" * 40)

# Output (printing a message)
print("Welcome to the Python learning path!")

# Taking user input
name = input("What is your name? ")
age = input("How old are you? ")

# You can see that input() always returns a string by default.
print(f"\nHello, {name}! You are {age} years old.")

# Converting input to integer for calculations
age_in_months = int(age) * 12
print(f"Did you know? You have lived for approximately {age_in_months} months!")

# Demonstrating formatted output
print(f"\nGreetings {name},\nYou are {age} years old, which is {age_in_months} months!")
