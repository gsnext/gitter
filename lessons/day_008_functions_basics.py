"""
Day 8: Functions - Basics

Learning Objectives:
- Learn to define and call functions
- Understand parameters and return values
- Practice writing reusable code
- Use default parameters

Expected Output:
Hello, Alice!
Sum: 15
Area: 50
"""

def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def calculate_area(length, width=10):
    """Calculate rectangle area with default width"""
    return length * width

# Using functions
message = greet("Alice")
print(message)

result = add_numbers(7, 8)
print(f"Sum: {result}")

area = calculate_area(5)
print(f"Area: {area}")

# Practice Exercise
# TODO: Write a function called 'multiply' that takes two numbers and returns their product
# TODO: Write a function called 'is_even' that returns True if a number is even
# TODO: Write a function with a default parameter
