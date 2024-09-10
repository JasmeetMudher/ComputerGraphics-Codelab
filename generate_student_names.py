import pandas as pd
from functions import log_computation


# Load the student data
def load_student_data(file_path):
    return pd.read_excel(file_path)


# Separate by gender
def split_by_gender(data):
    male_students = data[data['Gender'] == 'M']
    female_students = data[data['Gender'] == 'F']

    male_students.to_csv('output_files/male_students.csv', sep=',', index=False)
    male_students.to_csv('output_files/male_students.tsv', sep='\t', index=False)

    female_students.to_csv('output_files/female_students.csv', sep=',', index=False)
    female_students.to_csv('output_files/female_students.tsv', sep='\t', index=False)

    log_computation(f"Male students: {len(male_students)}")
    log_computation(f"Female students: {len(female_students)}")


# Main function
def main():
    student_data = load_student_data('input_files/test_file.xlsx')
    split_by_gender(student_data)


if __name__ == '__main__':
    main()
