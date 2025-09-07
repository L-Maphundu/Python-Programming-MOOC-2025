# write your solution here
def student_details(file):
    """Reads a csv file containing student id, first name
    and last name (in that order) and returns a dictionary
    of id (key) and full name (value)."""
    
    student_details = {}
    with open(file) as students:
        for student in students:
            student = student.strip()
            id, name, surname = student.split(';')

            if id == "id": #ignore the header row.
                continue

            student_details[id] = f"{name} {surname}"
    
    return student_details

def exercises(file):
    """Reads a csv file containing student id and exercises completed
    and return a dictionary of id (key) and aggregate of exercises (value)."""

    exercises = {}
    with open(file) as students:
        for student in students:
            student = student.strip()
            info = student.split(';')

            id = info[0]
            if id == "id":
                continue

            exercises_completed = info[1:]
            for i in range(len(exercises_completed)):
                exercises_completed[i] = int(exercises_completed[i])

            exercises[id] = sum(exercises_completed)

    return exercises
    
def main():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

    details = student_details(student_info)
    aggregates = exercises(exercise_data) 

    for id, aggregate in aggregates.items():
        if id in details:
            print(details[id], aggregate)

main()
