import pandas as pd
import re
import os
import logging
import json

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
    df['Special Character'] = df['Student Name'].apply(
        lambda name: 'yes' if re.search(r'[^a-zA-Z\s,]', name) else 'no')

    # Get a list of students with 'yes' (indicating special characters)
    special_students_list = df[df['Special Character'] == 'yes']['Student Name'].tolist()

    # Log students with special characters
    logging.info(f"Students with special characters: {special_students_list}")

    return df


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


def save_to_json(data, output):
    with open(output, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def combined_students_to_json(df):
    json_list = []
    df['DoB'] = df['DoB'].astype(str)
    for idx, row in df.iterrows():
        student_json = {
            "id": str(idx),
            "student_name": row['Student Name'],
            "additional_details": {
                "dob": row['DoB'],
                "gender": row['Gender'],
                "special_character": f"['{row['Special Character']}']",
            }
        }
        json_list.append(student_json)
    save_to_json(json_list, "output_files/combined_students.json")


def shuffled_students_to_json(df):
    # Shuffle the DataFrame
    df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df_shuffled['DoB'] = df_shuffled['DoB'].astype(str)

    # Change to JSON
    json_data = df_shuffled.to_dict(orient='records')

    save_to_json(json_data, "output_files/shuffled_students.json")


def main():
    # Setup logging to log student counts and special character names
    setup_logging('output_files/logs/computations.log')

    # Load data from Excel
    df = load_data('input_files/test_file.xlsx')

    # Generate unique email addresses
    df = generate_email(df)
    pd.set_option('display.max_columns', None)

    # Split students by gender and log counts
    male_students, female_students = split_gender(df)

    # Find students with special characters and log names
    df = find_special_characters(df)

    # Save all data to files (both CSV and TSV)
    save_to_files(df, male_students, female_students, 'output_files/')

    # Combine all the data in one JSON file
    combined_students_to_json(df)

    # One time shuffle of the data saved to JSON file
    shuffled_students_to_json(df)


if __name__ == "__main__":
    main()
