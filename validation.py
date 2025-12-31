import numbers

def validate_profile(profile):
    required_keys = ["name", "scores"]
    for key in required_keys:
        if key not in profile:
            raise KeyError(f"Missing key: {key}")
    if not isinstance(profile["scores"], dict):
        raise ValueError("Scores must be a dictionary")
    for subject, score in profile["scores"].items():
        if not isinstance(score, numbers.Number):
            raise ValueError(f"Score for {subject} is invalid")
    return True
