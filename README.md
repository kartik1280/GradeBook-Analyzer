# GradeBook Analyzer

GradeBook Analyzer is a Python tool designed to help educators, students, and developers efficiently manage and analyze student grades. You can enter student data manually or import it from a CSV file, then get detailed grade calculations, statistics, and summaries.

## Features

- Manual entry or CSV import of student names and marks
- Automatic grade assignment (A, B, C, D, F) based on score thresholds
- Calculates average, median, highest, and lowest scores
- Shows grade distribution and lists of passed/failed students
- Export analyzed results to a CSV file
- Simple, interactive command-line interface

## Getting Started

### Prerequisites

- Python 3.13.9 installed on your system

### Installation

1. Clone or download this repository.
2. Place your student marks CSV file (e.g., `student_marks.csv`) in the same directory as the script or provide the full path when prompted.

### Usage

Run the analyzer with the command:
python gradebook.py


Follow the on-screen menu:

- Select **1** for manual student entry.
- Select **2** to import student data from a CSV file.
- Select **q** to quit.

After entering data, the program displays a table with student names, marks, and grades, followed by statistics like average score, median, highest and lowest marks, grade distribution, and lists of passed and failed students.

You can repeat the analysis with new data sets or export results to a CSV (`gradebook_results.csv`).

## Example Input CSV (`student_marks.csv`)

Name,Marks
Kartik,85
Muskan,92
Rachit,78
Srikar,69
Kabir,54


## Sample Output Table

| Name    | Marks | Grade |
|---------|-------|-------|
| Kartik  | 85.00 | B     |
| Muskan  | 92.00 | A     |
| Rachit  | 78.00 | C     |
| Srikar  | 69.00 | D     |
| Kabir   | 54.00 | F     |

## Screenshots
![Output csv](https://github.com/user-attachments/assets/555520d5-2c3e-468e-bd10-217e72af7176)
![gradebook_result csv](https://github.com/user-attachments/assets/04f45bf4-101e-4b0a-93f4-49a02f029a5b)
![student_marks csv](https://github.com/user-attachments/assets/04d19aab-380b-4daa-8387-d5484e60199b)


## Author

Kartik Sharma  
Date: 04-11-2025

## License

This project is for learning purposes. Feel free to use and modify it with proper credit.


