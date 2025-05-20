# -------------------------------------------
# 🔁 Python Loops Tutorial
# -------------------------------------------

# Loops help us run a block of code multiple times.
# Two main types: for loop and while loop

# -------------------------------------------
# 🧱 For Loop
# -------------------------------------------

# Looping through a list
fruits = ["apple", "banana", "cherry"]

print("🍎 Fruit List:")
for fruit in fruits:
    print("-", fruit)

# Looping through a range of numbers
print("\n🔢 Numbers from 0 to 4:")
for i in range(5):  # 0 to 4
    print(i)

# Custom start and end
print("\n🔢 Numbers from 2 to 6:")
for i in range(2, 7):  # 2 to 6
    print(i)

# -------------------------------------------
# 🌀 While Loop
# -------------------------------------------

count = 0

print("\n🕒 While Loop Example:")
while count < 3:
    print("Count is", count)
    count += 1

# -------------------------------------------
# ❌ Break and ✅ Continue
# -------------------------------------------

print("\n🚪 Break Example:")
for number in range(10):
    if number == 5:
        break
    print(number)

print("\n⏭️ Continue Example:")
for number in range(5):
    if number == 2:
        continue
    print(number)

# -------------------------------------------
# 🔁 Nested Loops
# -------------------------------------------

print("\n🧮 Multiplication Table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ Use for loops to iterate over sequences (list, tuple, range, etc.)
# ✅ Use while loops when you don’t know how many times to repeat
# ✅ break exits the loop early
# ✅ continue skips current iteration
# ✅ Loops can be nested for complex logic
