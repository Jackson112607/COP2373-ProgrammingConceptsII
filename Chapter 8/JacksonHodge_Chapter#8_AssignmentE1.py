# This program lets instructors enter names and exam grades for the amount of students they have in a class. The program
# then writes the data to a csv file and displays what the csv file looks like in the console.

# Import the csv module.
import csv

# write_grades_csv gets input from the user and writes it to the csv file.
def write_grades_csv():
    # Get input for how many students to enter in the file.
    num_students = int(input("Enter the number of students: "))
    # t
    with open("grades.csv", "w", newline="") as csvfile:
        fieldnames = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # Get input for each field.
        for _ in range(num_students):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))
            # Write to the file.
            writer.writerow({
                "First Name": first_name,
                "Last Name": last_name,
                "Exam 1": exam1,
                "Exam 2": exam2,
                "Exam 3": exam3,
            })
    print("Grades written to grades.csv")

# read_grades_csv prints the file to the console to view.
def read_grades_csv():
    with open("grades.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print("{:<15} {:<15} {:<8} {:<8} {:<8}".format("First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"))
        print("-" * 56) #adjust length based on column width
        for row in reader:
            print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(
            row["First Name"], row["Last Name"], row["Exam 1"], row["Exam 2"], row["Exam 3"]
                ))

# Call the functions to run the program.
write_grades_csv()
read_grades_csv()