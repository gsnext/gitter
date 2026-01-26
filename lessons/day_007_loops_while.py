"""
Day 7: While Loops

Learning Objectives:
- Understand loop iteration
- Learn to iterate over sequences
- Practice loop control (break, continue)
- Use loops to solve problems

Expected Output:
Counting: 0 1 2 3 4
Fruits: apple banana cherry
Sum: 15
"""

# Basic for loop with range
print("Counting:", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", end=" ")
for fruit in fruits:
    print(fruit, end=" ")
print()

# Using loops for calculations
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# Loop with break
for i in range(10):
    if i == 5:
        break
    print(f"Number: {i}")

# Practice Exercise
# TODO: Create a loop that prints even numbers from 0 to 10
# TODO: Create a loop that calculates the product of numbers 1-5
