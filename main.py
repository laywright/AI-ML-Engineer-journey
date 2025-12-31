from logging_setup import setup_logging
from data_input import load_json_file, manual_input
from validation import validate_profile
from processing import average_score, top_students
from transformation import flatten_scores
import logging

def main():
    setup_logging()

    students = load_json_file("students.json") + manual_input()
    clean_students = []

    for student in students:
        try:
            validate_profile(student)
            clean_students.append(student)
        except (KeyError, ValueError) as e:
            logging.warning(f"Skipped student: {student.get('name', 'Unknown')} - {e}")
            continue

    print("Top students:", top_students(clean_students))
    print("Flattened scores for ML:", flatten_scores(clean_students))

if __name__ == "__main__":
    main()
