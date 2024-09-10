import pandas as pd
import json
import generate_email_addresses
import generate_student_names


def main():
    # Generate email addresses
    generate_email_addresses.main()

    # Separate students by gender
    generate_student_names.main()

    # Load student data
    student_data = pd.read_excel('input_files/test_file.xlsx')

    # Shuffle the student data
    shuffled_data = student_data.sample(frac=1).reset_index(drop=True)

    # Convert Timestamp to string if necessary
    for column in shuffled_data.columns:
        if pd.api.types.is_datetime64_any_dtype(shuffled_data[column]):
            shuffled_data[column] = shuffled_data[column].astype(str)

    # Convert DataFrame to the desired JSON format
    formatted_data = []
    for idx, row in shuffled_data.iterrows():
        record = {
            "id": str(idx),
            "student_name": row["Student Name"],
            "additional_details": {
                "dob": row["DoB"],
                "gender": row["Gender"],
                "special_character": ["no"]  # Adjust if you have special character handling logic
            }
        }
        formatted_data.append(record)

    # Save formatted data as JSON
    with open('output_files/shuffled_data.json', 'w') as json_file:
        json.dump(formatted_data, json_file, indent=4)

    # Save formatted data as JSONL
    with open('output_files/shuffled_data.jsonl', 'w') as jsonl_file:
        for record in formatted_data:
            jsonl_file.write(json.dumps(record) + '\n')



if __name__ == '__main__':
    main()
