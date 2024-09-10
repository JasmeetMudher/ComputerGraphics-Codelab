import re

# Function to sanitize names and remove special characters
def sanitize_name(name):
    return re.sub(r'[^a-zA-Z]', '', name)

# Function to generate an email address
def generate_email(first_name, last_name):
    email = f"{first_name[0].lower()}{last_name.lower()}@gmail.com"
    return email

# Function to split names into first letter of the last name (before comma) and the full last name (after comma)
def split_name(full_name):
    name_parts = full_name.split(', ')
    last_name_before_comma = sanitize_name(name_parts[0])
    last_word_after_comma = sanitize_name(name_parts[1].split()[-1])

    # Return the first letter of the last name and the full last word after the comma
    return last_name_before_comma[0], last_word_after_comma


# Function to log computations
def log_computation(message, log_file='output_files/logs/computations.log'):
    with open(log_file, 'a') as log:
        log.write(message + '\n')
