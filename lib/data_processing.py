def average_age(students):
    total = sum(s["age"] for s in students)
    return total / len(students)


def count_by_major(students):
    result = {}
    for s in students:
        major = s["major"]
        result[major] = result.get(major, 0) + 1
    return result