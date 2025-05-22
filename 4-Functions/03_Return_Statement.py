# -------------------------------------------
# 🔁 The return Statement in Python
# -------------------------------------------

# A function can send back a value using the `return` statement.
# This allows you to reuse the result later in your code.

# -------------------------------------------
# 1️⃣ Basic Return Example
# -------------------------------------------

def square(number):
    return number ** 2

result = square(4)
print("Square of 4:", result)

# -------------------------------------------
# 2️⃣ Returning Multiple Values
# -------------------------------------------

def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

x, y = calculate(10, 5)
print("Sum:", x)
print("Difference:", y)

# -------------------------------------------
# 3️⃣ Return vs Print
# -------------------------------------------

def print_sum(a, b):
    print("Sum (printed):", a + b)

def return_sum(a, b):
    return a + b

# Calling both
print_sum(3, 4)  # Just prints
total = return_sum(3, 4)
print("Sum (returned):", total)  # You can store or reuse this

# -------------------------------------------
# 4️⃣ Return Ends the Function
# -------------------------------------------

def test_return():
    print("Before return")
    return "This is returned"
    print("After return")  # This line will not run

print(test_return())

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ `return` sends a result back to the caller
# ✅ Functions can return one or multiple values
# ✅ `return` ends function execution
# ✅ Use `return` when you need the result later
