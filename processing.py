def average_score(profile):
    scores = profile["scores"].values()
    return sum(scores)/len(scores) if scores else 0

def top_students(students, threshold=80):
    top = []
    for student in students:
        avg = average_score(student)
        if avg >= threshold:
            top.append(student["name"])
    return top
