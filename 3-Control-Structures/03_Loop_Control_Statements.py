# -------------------------------------------
# 🔁 Loop Control Statements in Python
# -------------------------------------------

# Loop control statements allow us to alter the flow of loops:
# - break: Exit the loop immediately
# - continue: Skip the current iteration
# - pass: Placeholder that does nothing

# -------------------------------------------
# 🚪 break – Exit the loop early
# -------------------------------------------

print("🚪 break example:")
for number in range(1, 10):
    if number == 5:
        print("Breaking at 5")
        break
    print("Number:", number)

# -------------------------------------------
# ⏭️ continue – Skip this iteration
# -------------------------------------------

print("\n⏭️ continue example:")
for number in range(1, 6):
    if number == 3:
        print("Skipping 3")
        continue
    print("Number:", number)

# -------------------------------------------
# 🪫 pass – Do nothing (used as a placeholder)
# -------------------------------------------

print("\n🪫 pass example:")
for number in range(1, 4):
    if number == 2:
        pass  # Placeholder for future logic
    print("Number:", number)

# -------------------------------------------
# ✅ Using break in while loop
# -------------------------------------------

print("\n🔁 while loop with break:")
i = 1
while True:
    print("i =", i)
    i += 1
    if i > 3:
        break

# -------------------------------------------
# 🧠 Summary
# -------------------------------------------
# ✅ break → stops the loop completely
# ✅ continue → skips the current iteration
# ✅ pass → does nothing (useful for placeholders)
