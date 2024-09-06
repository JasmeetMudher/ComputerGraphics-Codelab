from generate_student_names import main as generate_student_names_main
from functions import setup_logging, log_male_female_count, log_special_characters


def main():
    setup_logging('output_files/logs/computations.log')
    generate_student_names_main()

    # Log the computations
    male_count = ...  # You need to determine how to get this value
    female_count = ...  # You need to determine how to get this value
    special_chars_names = ...  # You need to determine how to get this value
    log_male_female_count(male_count, female_count, 'output_files/logs/computations.log')
    log_special_characters(special_chars_names, 'output_files/logs/computations.log')


if __name__ == "__main__":
    main()
