
import re

def extract_numerical_values(input_text):
    # Use regular expression to find numerical values
    numerical_values = re.findall(r'\b\d+\b', input_text)

    # Convert the values to integers and return as a list
    numerical_list = [int(value) for value in numerical_values]

    return numerical_list

# Example usage:
input_text = """
    42
    18, 23
    abc 56 def
    9
"""




import matplotlib.pyplot as plt

# Define the raw percentage data
percentages = extract_numerical_values(input_text)




# Define grade categories and corresponding percentage ranges
grade_categories = [
    (95.01, 100, 'A+'),
    (85.01, 95, 'A'),
    (80.01, 85, 'A-'),
    (77.01, 80, 'B+'),
    (73.01, 77, 'B'),
    (70.01, 73, 'B-'),
    (67.01, 70, 'C+'),
    (63.01, 67, 'C'),
    (60.01, 63, 'C-'),
    (57.01, 60, 'D+'),
    (53.01, 57, 'D'),
    (50.01, 53, 'D-'),
    (0, 50, 'F')
]

# Initialize gradeCount hash map
gradeCount = {
    'F': 0,
    'D-': 0,
    'D': 0,
    'D+': 0,
    'C-': 0,
    'C': 0,
    'C+': 0,
    'B-': 0,
    'B': 0,
    'B+': 0,
    'A-': 0,
    'A': 0,
    'A+': 0,
}

# Iterate over percentages and update gradeCount
for percentage in percentages:
    for grade_range in grade_categories:
        min_range, max_range, grade = grade_range
        if min_range <= percentage <= max_range:
            gradeCount[grade] += 1
            break  # Break to avoid updating multiple grades for the same percentage



# Define grade colors
grade_colors = {
    'A+': 'blue',
    'A': 'green',
    'A-': 'lime',
    'B+': 'cyan',
    'B': 'yellow',
    'B-': 'orange',
    'C+': 'purple',
    'C': 'pink',
    'C-': 'magenta',
    'D+': 'brown',
    'D': 'red',
    'D-': 'maroon',
    'F': 'black'
}

grades = list(gradeCount.keys())
frequency = list(gradeCount.values())

# Create a bar plot
plt.bar(grades, frequency, color=[grade_colors[grade] for grade in grades])

# Adding labels and title
plt.xlabel('Letter Grade')
plt.ylabel('Frequency')
plt.title('Distribution of Letter Grades')

# Display the frequency on top of each bar
for i, v in enumerate(frequency):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom')

# Show the plot
plt.show()
