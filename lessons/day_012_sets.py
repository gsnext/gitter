"""
Day 12: Sets

Learning Objectives:
- Understand Python data structures
- Learn common operations
- Practice data manipulation
- Use appropriate data structure for tasks

Expected Output:
Items: [1, 2, 3, 4, 5]
Person: {'name': 'Alice', 'age': 25}
Unique: {1, 2, 3, 4, 5}
"""

# Lists - ordered, mutable
items = [1, 2, 3, 4, 5]
items.append(6)
print(f"Items: {items[:5]}")

# Dictionaries - key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {'name': '{person['name']}', 'age': {person['age']}}")

# Sets - unique elements
unique_numbers = {1, 2, 3, 3, 4, 5, 5}
print(f"Unique: {unique_numbers}")

# Tuples - immutable
coordinates = (10, 20)
x, y = coordinates

# Practice Exercise
# TODO: Create a dictionary representing a student with name, grades (list), and major
# TODO: Add a new grade to the grades list
# TODO: Create a set of unique words from a sentence
