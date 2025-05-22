# -------------------------------------------
# 🔍 Scope and Lifetime of Variables in Python
# -------------------------------------------

# 💡 Scope: Where a variable can be accessed in your code.
# 💡 Lifetime: How long the variable exists in memory.

# -------------------------------------------
# 1️⃣ Local Scope
# -------------------------------------------

def greet():
    name = "Tshigidimisa"  # Local variable
    print("Hello", name)

greet()
# print(name)  ❌ Error: 'name' is not accessible outside the function

# -------------------------------------------
# 2️⃣ Global Scope
# -------------------------------------------

role = "Data Analyst"  # Global variable

def show_role():
    print("Role:", role)  # Can access global variables

show_role()

# -------------------------------------------
# 3️⃣ Changing Global Variables Inside Functions
# -------------------------------------------

count = 0

def increment():
    global count  # Use global keyword to modify
    count += 1

increment()
print("Count:", count)

# -------------------------------------------
# 4️⃣ Variable Lifetime
# -------------------------------------------

def demo_lifetime():
    temp = 42  # temp is created when function is called
    print("Temp:", temp)

demo_lifetime()
# temp doesn't exist anymore here

# -------------------------------------------
# 5️⃣ Enclosing Scope (Nested Functions)
# -------------------------------------------

def outer():
    message = "Hello"

    def inner():
        print("Message from inner():", message)  # Can access outer function's variable

    inner()

outer()

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ Local scope – variables declared inside functions
# ✅ Global scope – variables declared outside all functions
# ✅ `global` keyword – allows modifying global variables inside a function
# ✅ Lifetime – variables exist as long as their scope is active
# ✅ Nested (enclosing) scope – inner functions can access outer variables
