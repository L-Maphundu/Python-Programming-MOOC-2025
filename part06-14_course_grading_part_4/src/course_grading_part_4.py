# tee ratkaisu tänne
def student_details(filename):
    """Reads a csv file containing student id, first name
    and last name (in that order) and returns a dictionary
    of id (key) and full name (value)."""
    
    student_details = {}
    with open(filename) as students:
        for student in students:
            student = student.strip()
            id, name, surname = student.split(';')

            if id == "id": #ignore the header row.
                continue

            student_details[id] = f"{name} {surname}"
    
    return student_details

def aggregator(filename):
    """Reads a csv file containing student id and exercises completed or exam points
    and returns a dictionary of id (key) and aggregate of exercises or aggregate exam points (value)."""

    exercises = {}
    with open(filename) as students:
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

def student_summary(details: dict, exercises: dict, exams: dict):
    """Returns a dictionary of full name (key) and summary statistics comprised of exercises and grades."""
    summary = {}
    boundaries = [15, 18, 21, 24, 28]

    for id, full_name in details.items():
        exercise_tot = exercises[id]
        exercise_points = int((exercise_tot*100/40)//10)
        exam_points = exams[id]
        total = exercise_points + exam_points
        
        grade = 0
        for boundary in boundaries:
            if total >= boundary:
                grade += 1

        summary[full_name] = [exercise_tot, exercise_points, exam_points, total, grade]

    return summary

def course_info(filename):
    """Reads a file containing course information and
     returns a course name and credit string
    """
    details = []
    with open(filename) as course_info:
        for line in course_info:
            info = line.split(':')
            details.append(info[1].strip())
    
    header = f"{details[0]}, {details[1]} credits"
    underline = "="*len(header)

    return header + "\n" + underline 

def main():
    student_info = input("Student information: ").strip()
    exercise_data = input("Exercises completed: ").strip()
    exam_data = input("Exam points: ").strip()
    course_details = input("Course information: ").strip()

    #populate the dictionaries needed by student_summary function.
    details = student_details(student_info)
    exercises = aggregator(exercise_data) 
    exams = aggregator(exam_data)
    
    summary = student_summary(details, exercises, exams)

    #Write course results.csv
    with open("results.csv", "w") as report_card:
        for id, fullname in details.items():
            if fullname in summary:
                report_card.write(f"{id};{fullname};{summary[fullname][-1]}\n")

    #Course information.
    course_name = course_info(course_details)

    #Write course results.txt
    with open("results.txt", "w") as results:
        results.write(course_name + "\n")
        results.write(f"{'name':30}exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    
        student = ""
        for full_name, stats in summary.items():
            student += f"{full_name:30}"
            for data in stats:
                student += f"{str(data):10}"
            results.write(student + "\n")
            student = ""

main()
