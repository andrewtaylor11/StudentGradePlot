from flask import Flask, render_template, request, send_file
import re
import io
import matplotlib.pyplot as plt

app = Flask(__name__)

def extract_numerical_values(input_text):
    # Use regex to find all numeric sequences, allowing for various separators
    numerical_values = re.findall(r'\b\d+(?:\.\d+)?\b', input_text.replace('\n', ' '))
    numerical_list = [float(value) for value in numerical_values]
    return numerical_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.form['input_data']
    grading_option = request.form['grading_option']

    percentages = extract_numerical_values(data)

    default_min_values = {
    'F': 0, 'D-': 50.01, 'D': 53.01, 'D+': 57.01, 'C-': 60.01, 'C': 63.01,
    'C+': 67.01, 'B-': 70.01, 'B': 73.01, 'B+': 77.01, 'A-': 80.01, 'A': 85.01, 'A+': 90.01
    }

    default_max_values = {
    'F': 50, 'D-': 53, 'D': 57, 'D+': 60, 'C-': 63, 'C': 67,
    'C+': 70, 'B-': 73, 'B': 77, 'B+': 80, 'A-': 85, 'A': 90, 'A+': 100
    }


    default_CHEM198min_values = {
    'F': 0, 'D-': 50.01, 'D': 53.01, 'D+': 57.01, 'C-': 60.01, 'C': 63.01,
    'C+': 67.01, 'B-': 70.01, 'B': 73.01, 'B+': 77.01, 'A-': 80.01, 'A': 85.01, 'A+': 95.01
    }

    default_CHEM198max_values = {
    'F': 50, 'D-': 53, 'D': 57, 'D+': 60, 'C-': 63, 'C': 67,
    'C+': 70, 'B-': 73, 'B': 77, 'B+': 80, 'A-': 85, 'A': 95, 'A+': 100
    }

    grade_ranges = {}
    # Set default or CHEM198 grade ranges based on the selected option
    if grading_option == 'default':
        for grade in ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']:
            min_value = default_min_values[grade]
            max_value = default_max_values[grade]
            grade_ranges[grade] = {'min': min_value, 'max': max_value}
    elif grading_option == 'CHEM198':
        for grade in ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']:
            min_value = default_CHEM198min_values[grade]
            max_value = default_CHEM198max_values[grade]
            grade_ranges[grade] = {'min': min_value, 'max': max_value}
    elif grading_option == 'custom':
        for grade in ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']:
            min_key = f"{grade}_min"
            max_key = f"{grade}_max"
            min_value = float(request.form[min_key]) if request.form[min_key] else None
            max_value = float(request.form[max_key]) if request.form[max_key] else None

            # If values are not provided, use the default values
            if min_value is None:
                min_value = default_min_values[grade]
            if max_value is None:
                max_value = default_max_values[grade]
            grade_ranges[grade] = {'min': min_value, 'max': max_value}




    gradeCount = {
        'F': 0, 'D-': 0, 'D': 0, 'D+': 0, 'C-': 0, 'C': 0,
        'C+': 0, 'B-': 0, 'B': 0, 'B+': 0, 'A-': 0, 'A': 0, 'A+': 0,
    }

    for percentage in percentages:
        for grade, grade_range in grade_ranges.items():
            min_range, max_range = grade_range['min'], grade_range['max']
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


    # Calculate the maximum frequency
    max_frequency = max(frequency)

    # Set the upper limit of the y-axis slightly higher than the maximum frequency
    upper_limit = max_frequency + (max_frequency/7)

    plt.bar(grades, frequency, color=[grade_colors[grade] for grade in grades])
    plt.xlabel('Letter Grade')
    plt.ylabel('Frequency')
    plt.title('Distribution of Letter Grades')

    for i, v in enumerate(frequency):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom')

    # Set y-axis limits
    plt.ylim(0, upper_limit)

    # Save the plot as an image in memory
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()

    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)



