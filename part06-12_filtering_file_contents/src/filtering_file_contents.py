# Write your solution here
def filter_solutions():
    """Reads the solutions.csv file and creates two files.
    'correct.csv' contains correct solutions to exercises from 'solutions.csv'
    and 'incorrect.csv' contains the incorrect ones."""

    with open("solutions.csv") as solutions, open("correct.csv", "w") as correct, open("incorrect.csv", "w") as incorrect:

        #Reads each line from the solutions.
        for line in solutions:
            line = line.strip()
            name, expression, result = line.split(";")
            
            #Perform the expression to check if it is correct by comparing to result.
            if "+" in expression:
                operation = expression.split("+")
                computation = int(operation[0]) + int(operation[1])
            else:
                operation = expression.split("-")
                computation = int(operation[0]) - int(operation[1])
            
            #Write the computation to the correct file according to whether the answer is correct or incorrct.
            if computation == int(result):
                correct.write(f"{line}\n")
            else:
                incorrect.write(f"{line}\n")
                
filter_solutions()
            

                

