from generate_student_names import main as generate_student_names_main
from functions import setup_logging, log_male_female_count, log_special_characters


def main():
    setup_logging('output_files/logs/computations.log')
    generate_student_names_main()

    # Log the computations
    male_count = ...
    female_count = ...
    special_chars_names = ...
    log_male_female_count(male_count, female_count, 'output_files/logs/computations.log')
    log_special_characters(special_chars_names, 'output_files/logs/computations.log')


if __name__ == "__main__":
    main()
