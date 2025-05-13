# 05_Comments_and_Docstrings.py
"""
Comments and Docstrings in Python

This script explains how to use comments and docstrings for better code documentation.
"""

# Single-line comment: A brief explanation for a specific line of code
print("Hello, world!")  # This prints 'Hello, world!' to the console

# Multi-line comment (can also use triple quotes)
# This is a multi-line comment.
# It allows you to explain more complex logic or add additional details
# over multiple lines.
#
# It does not affect the execution of the program.

# Docstrings: Used to describe the purpose of a module, class, or function.
def greet(name):
    """
    This function greets the user by name.

    Parameters:
    name (str): The name of the person to greet

    Returns:
    None
    """
    print(f"Hello, {name}!")

# Calling the function
greet("Tshigidimisa")

# To view the docstring of the function, use the help() function:
help(greet)
