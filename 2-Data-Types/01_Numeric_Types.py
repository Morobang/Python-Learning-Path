# ---------------------------------------
# 📘 Python Numeric Data Types Tutorial
# ---------------------------------------

# Python has three main numeric types:
# 1. int – Whole numbers (e.g., 5, -3, 100)
# 2. float – Decimal numbers (e.g., 3.14, -0.99)
# 3. complex – Numbers with real and imaginary parts (e.g., 2 + 3j)

# ---------------------------------------
# 🔢 Integer (int)
# ---------------------------------------

age = 25
print("Age (int):", age)
print("Type of age:", type(age))

# ---------------------------------------
# 🔣 Float (float)
# ---------------------------------------

temperature = 36.6
print("\nTemperature (float):", temperature)
print("Type of temperature:", type(temperature))

# ---------------------------------------
# 🧮 Complex (complex)
# ---------------------------------------

z = 2 + 3j
print("\nComplex Number:", z)
print("Real part:", z.real)
print("Imaginary part:", z.imag)
print("Type of z:", type(z))

# ---------------------------------------
# 🔄 Type Conversion
# ---------------------------------------

# Convert int to float
num = 7
num_float = float(num)
print("\nConvert int to float:", num_float)

# Convert float to int (note: decimal is truncated)
pi = 3.14159
pi_int = int(pi)
print("Convert float to int:", pi_int)

# ---------------------------------------
# 📌 Numeric Operations
# ---------------------------------------

a = 10
b = 3

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (remainder):", a % b)
print("Exponentiation:", a ** b)
