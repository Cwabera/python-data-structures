from lib.student_data import get_students
from lib.filters import filter_by_major
from lib.data_processing import average_age
from lib.set_operations import unique_majors
from lib.data_generator import student_generator


def main():
    students = get_students()

    print("All Students:")
    print(students)

    print("\nCS Students:")
    print(filter_by_major(students, "CS"))

    print("\nAverage Age:")
    print(average_age(students))

    print("\nUnique Majors:")
    print(unique_majors(students))

    print("\nGenerator Output:")
    for s in student_generator(students):
        print(s["name"])


if __name__ == "__main__":
    main()