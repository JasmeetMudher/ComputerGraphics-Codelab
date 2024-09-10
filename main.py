from generate_student_names import main as generate_student_names_main, setup_logging


def main():
    setup_logging('output_files/logs/computations.log')
    generate_student_names_main()

if __name__ == "__main__":
    main()
