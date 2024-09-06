import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_male_female_count(male_count, female_count, log_file):
    logging.info(f"Number of male students: {male_count}")
    logging.info(f"Number of female students: {female_count}")

def log_special_characters(names, log_file):
    logging.info(f"Names with special characters: {names}")
