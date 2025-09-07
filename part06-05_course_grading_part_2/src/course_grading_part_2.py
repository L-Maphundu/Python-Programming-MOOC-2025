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

def aggregator(file):
    """Reads a csv file containing student id and exercises completed or exam points
    and returns a dictionary of id (key) and aggregate of exercises or aggregate exam points (value)."""

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

def student_grades(details: dict, exercises: dict, exams: dict):
    """Returns a dictionary of full name (key) and grade (value)
    given 3 dictionaries of: deatils (id & full name), exams (id & exam points)
    and exercises (id & exercises aggregate)."""
    grades = {}
    boundaries = [15, 18, 21, 24, 28]

    for id, full_name in details.items():
        total = (exercises[id]*100/40)//10 + exams[id]
        grade = 0

        for boundary in boundaries:
            if total >= boundary:
                grade += 1

        grades[full_name] = grade

    return grades
        
def main():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
     
    #populate the dictionaries needed by student_grades function.
    details = student_details(student_info)
    exercises = aggregator(exercise_data) 
    exams = aggregator(exam_data)

    grades = student_grades(details, exercises, exams)

    for full_name, grade in grades.items():
        print(full_name, grade)

main()
