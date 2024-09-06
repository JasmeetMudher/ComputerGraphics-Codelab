# This file will define any constraints or validation checks.

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError(f"Invalid email format: {email}")

def validate_name(name):
    if not name.isalpha() and ' ' not in name:
        raise ValueError(f"Invalid name format: {name}")
