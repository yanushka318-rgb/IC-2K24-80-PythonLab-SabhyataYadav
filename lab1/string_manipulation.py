# This program takes a full name as input and prints it
# in uppercase, lowercase, and displays its length.

full_name = input("Enter your full name: ")

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))

# Using additional string methods
print("Title Case:", full_name.title())
print("Without Extra Spaces:", full_name.strip())
