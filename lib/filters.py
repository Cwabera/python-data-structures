def filter_by_major(students, major):
    return [s for s in students if s["major"] == major]


def filter_by_course(students, course):
    return [s for s in students if course in s["courses"]]