def flatten_scores(students):
    flattened = []
    for student in students:
        flat = list(student["scores"].values())
        flattened.append(flat)
    return flattened
