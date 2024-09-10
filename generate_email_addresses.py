# generate_email_addresses.py
import pandas as pd
import re


def clean_name(name):
    """Remove any special characters and convert name to lowercase."""
    return re.sub(r'[^a-zA-Z]', '', name).lower()


def generate_email(df):
    # Initialize the 'Email Address' column
    df['Email Address'] = ''

    # Set to track existing emails to ensure uniqueness
    email_addresses = set()

    for _, row in df.iterrows():
        # Extract the name parts
        name_parts = row['Student Name'].split(', ')

        # Ensure there are enough parts to extract first and last names
        if len(name_parts) > 1:
            full_name_parts = name_parts[1].split()

            if len(full_name_parts) > 1:
                first_name = name_parts[0]
                last_name = full_name_parts[-1]
                email_base = f"{clean_name(first_name[0])}{clean_name(last_name)}@gmail.com"
            else:
                email_base = f"{clean_name(full_name_parts[0])}@gmail.com"
        else:
            email_base = "unknown@gmail.com"

        # Ensure unique email addresses
        email = email_base
        count = 1
        while email in email_addresses:
            email = f"{email_base.split('@')[0]}{count}@gmail.com"
            count += 1
        email_addresses.add(email)

        df.at[_, 'Email Address'] = email

    return df
