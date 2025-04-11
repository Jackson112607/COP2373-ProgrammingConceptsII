# This program takes an existing .csv file with students' grades and determines the mean grade, median grade, standard
# deviation of grades, minimum grade, maximum grade, and the overall pass percentage for each exam. Then, prints overall
# statistics for all exams as well.

# Import the numpy module.
import numpy as np
import csv

# Load the grades for each exam from the csv file.
def load_grades_from_csv(file_path="grades.csv"):
    grades = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numeric_row = [float(grade) for grade in row if grade.isdigit() or (grade.startswith('-') and grade[1:].isdigit()) or ('.' in grade and all(c.isdigit() for c in grade.replace('.', '')))]
            if numeric_row:
                    grades.append(numeric_row)
    return np.array(grades)

# Analyze the grades in a numpy array and print the data.
def analyze_grades(grades_array):
    if grades_array.size == 0:
        print("No grade data to analyze.")
        return

    num_exams = grades_array.shape[1]
    num_students = grades_array.shape[0]

    print("First few rows of the dataset:")
    print(grades_array[:5])
    print("\n")

    print("Statistics for each exam:")
    for i in range(num_exams):
        exam_grades = grades_array[:, i]
        print(f"Exam {i+1}:")
        print(f"  Mean: {np.mean(exam_grades):.2f}")
        print(f"  Median: {np.median(exam_grades):.2f}")
        print(f"  Standard Deviation: {np.std(exam_grades):.2f}")
        print(f"  Minimum: {np.min(exam_grades):.2f}")
        print(f"  Maximum: {np.max(exam_grades):.2f}")
        passed = np.sum(exam_grades >= 60)
        failed = np.sum(exam_grades < 60)
        print(f"  Passed: {passed}")
        print(f"  Failed: {failed}")
        print()

    all_grades = grades_array.flatten()
    print("Overall statistics for all exams:")
    print(f"  Mean grade: {np.mean(all_grades):.2f}")
    print(f"  Median grade: {np.median(all_grades):.2f}")
    print(f"  Standard deviation of grades: {np.std(all_grades):.2f}")
    print(f"  Minimum grade: {np.min(all_grades):.2f}")
    print(f"  Maximum grade: {np.max(all_grades):.2f}")

    overall_passed = np.sum(all_grades >= 60)
    total_grades = all_grades.size
    overall_pass_percentage = (overall_passed / total_grades) * 100 if total_grades > 0 else 0
    print(f"Overall pass percentage: {overall_pass_percentage:.2f}%")


def main():
    file_path = "grades.csv"
    student_grades = load_grades_from_csv(file_path)
    if student_grades.size > 0:
        analyze_grades(student_grades)

main()