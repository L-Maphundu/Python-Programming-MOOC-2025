# Write your solution here
def add_student(students: dict, name: str):
    """Adds a student to the database."""
    if name not in students:
        students[name] = []
    else:
        print("The student already exists.")

def add_course(students: dict, name: str, courseIn: tuple):
    """Adds students' courses and their respective grades (courseIn). Does not add the course if the grade is 0
    or the new grade is lower than the previous grade in case of an existing course."""
    courses = (students[name])[:]
    courseNames = []
    if courses == [] and courseIn[1] > 0:
        students[name].append(courseIn)  

    elif courseIn[1] > 0:
        for course in courses:
            courseNames.append(course[0])

        if courseIn[0] in courseNames:
            for course in courses:
                if course[0] == courseIn[0] and courseIn[1] > course[1]:
                    students[name].remove(course)
                    students[name].append(courseIn)
        else:
            students[name].append(courseIn)

def summary(students):
    most_courses = 0
    name = ""

    for student, courses in students.items():
        if len(courses) > most_courses:
            name = student
            most_courses = len(courses)
    
    highest = 0
    best_student = ""
    for student, courses in students.items():
        tot = 0
        for course in courses: #calculates the aggregate for the student.
            tot += course[1]

        avg = tot/len(courses)
        if avg > highest:
            best_student = student
            highest = avg
            
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses} {name}")
    print(f"best average grade {highest:.1f} {best_student}")
    
def print_student(students: dict, name: str):

    if name not in students:
        print(f"{name}: no such person in the database")
    elif students[name] == []:
        print(f"{name}:", " no completed courses", sep="\n")

    else:
        tot = 0 #The aggregate of all the courses taken
        completed_courses = len(students[name]) #Number of courses completed

        print(f"{name}:", f" {completed_courses} completed courses:",sep="\n")
        for course in students[name]:
            tot += course[1]
            print(f"  {course[0]} {course[1]}")
        
        print(f" average grade {(tot/completed_courses):.1f}") #Calculates and prints the average grade

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)