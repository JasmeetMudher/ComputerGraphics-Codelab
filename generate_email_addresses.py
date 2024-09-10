import pandas as pd
from functions import split_name, generate_email, log_computation


# Load the student data
def load_student_data(file_path):
    return pd.read_excel(file_path)


# Generate emails and save them
def generate_emails(data):
    emails = []
    for index, row in data.iterrows():
        first_name, last_name = split_name(row['Student Name'])
        email = generate_email(first_name, last_name)
        emails.append([row['Student Number'], row['Student Name'], email])
        log_computation(f"Generated email for {row['Student Name']}: {email}")

    email_df = pd.DataFrame(emails, columns=['Student Number', 'Student Name', 'Email Address'])
    email_df.to_csv('output_files/email_addresses.csv', sep=',', index=False)
    email_df.to_csv('output_files/email_addresses.tsv', sep='\t', index=False)
    log_computation("Email generation complete and saved to CSV and TSV files.")


# Main function
def main():
    student_data = load_student_data('input_files/test_file.xlsx')
    generate_emails(student_data)


if __name__ == '__main__':
    main()
