# Write your solution here
def grade(exam,overall):
    distribution = [0, 0, 0, 0, 0, 0]

    for i in range(len(exam)):
        if exam[i] < 10 or overall[i] < 15:
            index = 5
        elif overall[i] < 18:
            index = 4
        elif overall[i] < 21:
            index = 3
        elif overall[i] < 24:
            index = 2
        elif overall[i] < 28:
            index = 1
        else:
            index = 0
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

    stats = (grade(exams, overall))
    pass_rate = (sum(stats[:5])/sum(stats))*100

    print("Statistics:")
    print(f"Points average: {sum(overall)/len(overall)} ")
    print(f"Pass percentage: {pass_rate:.1f}")
    print("Grade distribution: ")
    for i in range(6):
        print(" "*2, f"{5-i}: ", "*"*stats[i], sep="")

main()
