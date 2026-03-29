def student_generator(students):
    for student in students:
        yield student


def students_above_age(students, age):
    return (s for s in students if s["age"] > age)