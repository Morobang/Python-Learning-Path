# ---------------------------------------
# 📘 Python Dictionary Data Type Tutorial
# ---------------------------------------

# A dictionary is an unordered, mutable collection of key-value pairs.
# Each key must be unique and hashable.

# ---------------------------------------
# 🧱 Creating Dictionaries
# ---------------------------------------

person = {
    "name": "Tshigidimisa",
    "age": 25,
    "profession": "Data Analyst"
}

empty_dict = {}  # or use dict()

print("Person Dictionary:", person)

# ---------------------------------------
# 🔍 Accessing Values
# ---------------------------------------

print("\nName:", person["name"])
print("Age:", person.get("age"))
print("Country (not found):", person.get("country", "Not specified"))

# ---------------------------------------
# 🛠️ Modifying Dictionaries
# ---------------------------------------

person["age"] = 26  # Update existing
person["city"] = "Polokwane"  # Add new

print("\nUpdated Person Dictionary:", person)

# ---------------------------------------
# ➖ Removing Elements
# ---------------------------------------

del person["profession"]
removed_city = person.pop("city")

print("After deleting 'profession':", person)
print("Popped city:", removed_city)

# ---------------------------------------
# 🔁 Looping Through Dictionaries
# ---------------------------------------

print("\nLooping through keys and values:")
for key, value in person.items():
    print(f"{key}: {value}")

# ---------------------------------------
# ✅ Dictionary Methods Summary
# ---------------------------------------

keys = person.keys()
values = person.values()
items = person.items()

print("\nKeys:", list(keys))
print("Values:", list(values))
print("Items:", list(items))

# ---------------------------------------
# 🧠 Dictionary Use Cases
# ---------------------------------------

# Counting items
word_count = {"python": 3, "data": 5}
word_count["python"] += 1  # Update count
print("\nWord Count Example:", word_count)

# Nesting (Dictionary inside another)
student = {
    "name": "Lebo",
    "grades": {
        "math": 85,
        "science": 92
    }
}
print("Nested Dictionary (grades):", student["grades"]["math"])

# ---------------------------------------
# 🧠 Summary
# ---------------------------------------
# ✅ Dicts are key-value stores
# ✅ Mutable, unordered (Python 3.7+ maintains insertion order)
# ✅ Common methods: get(), pop(), keys(), values(), items()
# ✅ Perfect for structured data like JSON
