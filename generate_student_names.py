import pandas as pd
import re
import os
import logging

from generate_email_addresses import generate_email


def setup_logging(log_file):
    """Set up logging configuration."""
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def load_data(file_path):
    """Load data from the Excel file."""
    return pd.read_excel(file_path)


def split_gender(df):
    """Split students based on gender."""
    male_students = df[df['Gender'].str.lower().isin(['male', 'm'])]
    female_students = df[df['Gender'].str.lower().isin(['female', 'f'])]

    # Log the counts of male and female students
    logging.info(f"Total Male Students: {len(male_students)}")
    logging.info(f"Total Female Students: {len(female_students)}")

    return male_students, female_students


def find_special_characters(df):
    """Find students with special characters in their names."""
    pattern = re.compile(r'[^a-zA-Z\s]')
    special_chars_students = df[df['Student Name'].apply(lambda x: bool(pattern.search(x)))]

    # Log students with special characters
    special_students_list = special_chars_students['Student Name'].tolist()
    logging.info(f"Students with special characters: {special_students_list}")

    return special_chars_students


def save_to_files(df, male_students, female_students, output_dir):
    """Save the DataFrame to CSV and TSV files."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the main dataframe with email addresses
    df.to_csv(os.path.join(output_dir, 'email_addresses.csv'), index=False)
    df.to_csv(os.path.join(output_dir, 'email_addresses.tsv'), sep='\t', index=False)

    # Save male and female lists separately in both CSV and TSV formats
    male_students.to_csv(os.path.join(output_dir, 'male_students.csv'), index=False)
    male_students.to_csv(os.path.join(output_dir, 'male_students.tsv'), sep='\t', index=False)

    female_students.to_csv(os.path.join(output_dir, 'female_students.csv'), index=False)
    female_students.to_csv(os.path.join(output_dir, 'female_students.tsv'), sep='\t', index=False)


def main():
    # Setup logging to log student counts and special character names
    setup_logging('output_files/logs/computations.log')

    # Load data from Excel
    df = load_data('input_files/test_file.xlsx')

    # Generate unique email addresses
    df = generate_email(df)

    # Split students by gender and log counts
    male_students, female_students = split_gender(df)

    # Find students with special characters and log names
    special_chars_students = find_special_characters(df)

    # Save all data to files (both CSV and TSV)
    save_to_files(df, male_students, female_students, 'output_files/')


if __name__ == "__main__":
    main()
