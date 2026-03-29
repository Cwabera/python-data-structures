def unique_majors(students):
    return {s["major"] for s in students}


def all_courses(students):
    courses = set()
    for s in students:
        courses.update(s["courses"])
    return courses


def common_courses(student1, student2):
    return set(student1["courses"]) & set(student2["courses"])