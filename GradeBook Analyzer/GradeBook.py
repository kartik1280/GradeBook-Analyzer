# gradebook.py
# Author: Kartik Sharma
# Date: 04-11-2025
# Title: GradeBook Analyzer 

import csv

def print_welcome():
    print("="*35)
    print("Welcome to the GradeBook Analyzer")
    print("="*35)
    print("Options:\n 1 - Manual Student Entry\n 2 - Import from CSV\n q - Quit\n")


def manual_entry():
    marks = {}
    n = int(input("How many students to enter? "))
    for i in range(n):
        name = input(f"Student {i+1} name: ").strip()
        score = float(input(f"Student {i+1} marks: "))
        marks[name] = score
    return marks

def csv_import(filename):
    marks = {}
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            if len(row) >= 2:
                marks[row[0].strip()] = float(row[1])
    return marks

def calculate_average(marks):
    return round(sum(marks.values()) / len(marks), 2) if marks else 0

def calculate_median(marks):
    vals = sorted(marks.values())
    if not vals:
        return 0
    mid = len(vals) // 2
    if len(vals) % 2 == 0:
        return (vals[mid-1] + vals[mid]) / 2
    else:
        return vals[mid]

def find_max_score(marks):
    mx = max(marks.values())
    students = [name for name, score in marks.items() if score == mx]
    return students, mx

def find_min_score(marks):
    mn = min(marks.values())
    students = [name for name, score in marks.items() if score == mn]
    return students, mn

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades):
    dist = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades.values():
        dist[grade] += 1
    return dist

def pass_fail_lists(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed

def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-"*32)
    for name in marks:
        print(f"{name:<15}\t{marks[name]:<5.2f}\t{grades[name]}")

def export_to_csv(marks, grades, filename="gradebook_results.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for name in marks:
            writer.writerow([name, marks[name], grades[name]])
    print(f"\nResults successfully exported to '{filename}'")

def main():
    while True:
        print_welcome()
        choice = input("Enter choice: ").strip().lower()
        if choice == '1':
            marks = manual_entry()
        elif choice == '2':
            filename = input("Enter CSV filename/path: ").strip()
            marks = csv_import(filename)
        elif choice == 'q':
            print("Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if not marks:
            print("No data entered or loaded. Please try again.")
            continue

        grades = assign_grades(marks)
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_students, max_score = find_max_score(marks)
        min_students, min_score = find_min_score(marks)
        distribution = grade_distribution(grades)
        passed, failed = pass_fail_lists(marks)

        print_table(marks, grades)

        print(f"\nStatistics:")
        print(f"Average Score: {avg}")
        print(f"Median Score: {med}")
        print(f"Highest Score: {max_score} by {', '.join(max_students)}")
        print(f"Lowest Score: {min_score} by {', '.join(min_students)}")
        print(f"Grade Distribution: {', '.join([f'{k}: {v}' for k,v in distribution.items()])}")
        print(f"Passed students ({len(passed)}): {', '.join(passed)}")
        print(f"Failed students ({len(failed)}): {', '.join(failed)}")

        cont = input("\nDo you want to analyze another set? (y/n): ").strip().lower()
        if cont != 'y':
            export = input("Export results to CSV? (y/n): ").strip().lower()
            if export == 'y':
                export_to_csv(marks, grades)
            print("Thank you for using GradeBook Analyzer!")
            break

if __name__ == "__main__":
    main()