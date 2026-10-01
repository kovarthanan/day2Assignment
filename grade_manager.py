students = []


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    while True:
        mark_input = input("Enter mark (0-100): ").strip()

        try:
            mark = float(mark_input)

            if mark < 0 or mark > 100:
                print("Invalid mark. Please enter a mark between 0 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")


    grade = calculate_grade(mark)

    students.append({
        "name": name,
        "mark": mark,
        "grade": grade
    })

    print(f"Student '{name}' added successfully.")


def show_results():
    if not students:
        print("\nNo students have been added yet.")
        return

    print("\n" + "=" * 40)
    print(f"{'Name':<20}{'Mark':<10}{'Grade':<10}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:<10.2f}"
            f"{student['grade']:<10}"
        )

    print("-" * 40)

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Class Average : {average:.2f}")
    print(f"Highest Mark  : {highest:.2f}")
    print(f"Lowest Mark   : {lowest:.2f}")
    print("=" * 40)


def main():
    while True:
        print("\nStudent Grade Manager")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

