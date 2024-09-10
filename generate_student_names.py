import pandas as pd
from functions import log_computation, sanitize_name, generate_email, split_name
import re

# Load the student data
def load_student_data(file_path):
    return pd.read_excel(file_path)


# Find students with special characters and log them
def find_special_characters(df):
    df['Special Character'] = df['Student Name'].apply(
        lambda name: 'yes' if re.search(r'[^a-zA-Z\s,]', name) else 'no'
    )

    # Get a list of students with 'yes' (indicating special characters)
    special_students_list = df[df['Special Character'] == 'yes']['Student Name'].tolist()

    # Log students with special characters
    log_computation(f"Students with special characters: {', '.join(special_students_list)}")

    return df


# Separate by gender and log special characters
def split_by_gender(data):
    male_students = data[data['Gender'].str.upper() == 'M']
    female_students = data[data['Gender'].str.upper() == 'F']

    # Save to CSV and TSV files
    male_students.to_csv('output_files/male_students.csv', sep=',', index=False)
    male_students.to_csv('output_files/male_students.tsv', sep='\t', index=False)

    female_students.to_csv('output_files/female_students.csv', sep=',', index=False)
    female_students.to_csv('output_files/female_students.tsv', sep='\t', index=False)

    # Log counts of male and female students
    log_computation(f"Male students: {len(male_students)}")
    log_computation(f"Female students: {len(female_students)}")

    # Find and log special characters
    data = find_special_characters(data)


# Main function
def main():
    # Load student data
    student_data = load_student_data('input_files/test_file.xlsx')

    # Split by gender and handle special characters
    split_by_gender(student_data)


if __name__ == '__main__':
    main()
