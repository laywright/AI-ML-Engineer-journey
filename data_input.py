import json

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def manual_input():
    students = []
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        try:
            math = int(input("Enter Math score: "))
            english = int(input("Enter English score: "))
            students.append({"name": name, "scores": {"Math": math, "English": english}})
        except ValueError:
            print("Invalid score, try again.")
    return students
