# Write your solution here
def grade(exam,overall):
    """Takes in two list, exam scores (exam)
    and overall scores (overall) and returns a list of grades 
    distribtution for the course."""
    
    #Stores the grades where index 0 correspends to grade 0 (fail) and index 5 is grade 5.
    distribution = [0, 0, 0, 0, 0, 0]

    for i in range(len(exam)):
        if exam[i] < 10 or overall[i] < 15:
            index = 0
        elif overall[i] < 18:
            index = 1
        elif overall[i] < 21:
            index = 2
        elif overall[i] < 24:
            index = 3
        elif overall[i] < 28:
            index = 4
        else:
            index = 5
        distribution[index] += 1
    
    return distribution

def main():
    exams = []
    overall = []

    while True:
        results = input("completed: ").strip()
        if results == "":
            break

        scores = results.split(" ")
        exams.append(int(scores[0]))
        overall.append(int(scores[0]) + int(scores[1])//10)

    if overall != []:
        stats = (grade(exams, overall))
        pass_rate = (sum(stats[1:])/sum(stats))*100

        print("Statistics:")
        print(f"Points average: {sum(overall)/len(overall)} ")
        print(f"Pass percentage: {pass_rate:.1f}")
        print("Grade distribution: ")
        for i in range(5,-1,-1):
            print(" "*2, f"{i}: ", "*"*stats[i], sep="")
    else:
        print("No results were entered.")

main()
