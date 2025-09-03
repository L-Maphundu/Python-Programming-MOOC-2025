# Write your solution here
students = {} #The dictionary storing students' information

def add_student(students: dict, name: str):
    """Adds a student to the database."""
    if name not in students:
        students[name] = []
    else:
        print("The student already exists.")

def add_course(students: dict, name: str, courseIn: tuple):
    """Adds students' courses and their respective grades (courseIn). Does not add the course if the grade is 0
    or the new grade is lower than the previous grade in case of an existing course."""

    if students[name] == []:
        students[name].append(courseIn)   

def print_student(students: dict, name: str):

    if name not in students:
        print(f"{name}: no such person in the database")
    elif students[name] == []:
        print(f"{name}:", " no completed courses", sep="\n")

    else:
        tot = 0 #The aggregate of all the courses taken
        completed_courses = len(students[name]) #Number of completed courses

        print(f"{name}:", f" {completed_courses} completed courses:",sep="\n")
        for course in students[name]:
            tot += course[1]
            print(f"  {course[0]} {course[1]}")
        
        print(f" average grade {(tot/completed_courses):.1f}") #Calculates and prints the average grade

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 23))
    print_student(students, "Peter")