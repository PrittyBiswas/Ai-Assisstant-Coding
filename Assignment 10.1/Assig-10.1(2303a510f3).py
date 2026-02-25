"""
Lab: Code Review and Quality Enhancement Using AI
This file contains solutions for:
1. Syntax and Logic Error Fixing
2. PEP 8 Compliance Refactoring
3. Readability Enhancement
"""


# --------------------------------------------------
# Task 1: Syntax and Logic Errors Fix
# --------------------------------------------------

def calc_average(marks):
    """
    Calculate the average score of a student.
    Handles empty list to avoid division by zero.
    """
    if len(marks) == 0:
        return 0

    total = 0
    for mark in marks:
        total += mark

    average = total / len(marks)
    return average


marks_list = [85, 90, 78, 92]
print("Average Score is:", calc_average(marks_list))


# --------------------------------------------------
# Task 2: PEP 8 Compliance
# --------------------------------------------------

def area_of_rect(length, breadth):
    """
    Calculate the area of a rectangle.
    """
    return length * breadth


print("Area of Rectangle:", area_of_rect(10, 20))


# --------------------------------------------------
# Task 3: Readability Enhancement
# --------------------------------------------------

def calculate_percentage(amount, percentage):
    """
    Calculate the percentage value of a given amount.
    """
    return (amount * percentage) / 100


total_amount = 200
percentage_value = 15

print("Calculated Percentage Value:",
      calculate_percentage(total_amount, percentage_value))