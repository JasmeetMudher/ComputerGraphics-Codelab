# generate_student_names.py
import pandas as pd
import re
import os  # Import os module

from generate_email_addresses import generate_email


def load_data(file_path):
    return pd.read_excel(file_path)


def split_gender(df):
    male_students = df[df['Gender'].str.lower() == 'male']
    female_students = df[df['Gender'].str.lower() == 'female']
    return male_students, female_students


def find_special_characters(df):
    pattern = re.compile(r'[^a-zA-Z\s]')
    special_chars_students = df[df['Student Name'].apply(lambda x: bool(pattern.search(x)))]
    return special_chars_students


def save_to_files(df, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df.to_csv(os.path.join(output_dir, 'email_addresses.csv'), index=False)
    df.to_csv(os.path.join(output_dir, 'email_addresses.tsv'), sep='\t', index=False)


def main():
    df = load_data('input_files/test_file.xlsx')
    df = generate_email(df)
    male_students, female_students = split_gender(df)
    special_chars_students = find_special_characters(df)
    save_to_files(df, 'output_files/')
    # You would also need to save the male/female lists, special characters lists, and other outputs as required.


if __name__ == "__main__":
    main()
