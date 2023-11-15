# main.py
from flask import Flask, request, jsonify, send_file
import re
import matplotlib.pyplot as plt
import io

app = Flask(__name__)


@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.form.get('data')

def extract_numerical_values(input_text):
    numerical_values = re.findall(r'\b\d+\b', input_text)
    numerical_list = [int(value) for value in numerical_values]
    return numerical_list


    percentages = extract_numerical_values(data)

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

    gradeCount = {
        'F': 0, 'D-': 0, 'D': 0, 'D+': 0, 'C-': 0, 'C': 0,
        'C+': 0, 'B-': 0, 'B': 0, 'B+': 0, 'A-': 0, 'A': 0, 'A+': 0,
    }

    for percentage in percentages:
        for grade_range in grade_categories:
            min_range, max_range, grade = grade_range
            if min_range <= percentage <= max_range:
                gradeCount[grade] += 1
                break

    grade_colors = {
        'A+': 'blue', 'A': 'green', 'A-': 'lime', 'B+': 'cyan',
        'B': 'yellow', 'B-': 'orange', 'C+': 'purple', 'C': 'pink',
        'C-': 'magenta', 'D+': 'brown', 'D': 'red', 'D-': 'maroon',
        'F': 'black'
    }

    grades = list(gradeCount.keys())
    frequency = list(gradeCount.values())

    plt.bar(grades, frequency, color=[grade_colors[grade] for grade in grades])
    plt.xlabel('Letter Grade')
    plt.ylabel('Frequency')
    plt.title('Distribution of Letter Grades')

    for i, v in enumerate(frequency):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom')

    # Save the plot as an image in memory
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()

    # Return the image file
    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

