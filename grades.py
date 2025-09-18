# Program Name: grades.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: 2
# Due Date: 09/19/ 2025
# Purpose: python program that calculates the final averages for a group of students and print the results in descending order by grade. 
# Used Python module and chapters.

def calculate_averages(filename):
    students = []

    # Open and read the input file
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            scores = list(map(int, parts[1:]))
            average = sum(scores) / len(scores)
            students.append((name, average))

    # Sort by average in descending order
    students.sort(key=lambda x: x[1], reverse=True)

    # Print results
    for name, avg in students:
        print(f"{name} {avg:.2f}")


# Run the program using "input.txt"
calculate_averages("input.txt")
