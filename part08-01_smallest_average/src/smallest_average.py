# Write your solution here

def smallest_average(person1: dict, person2: dict, person3: dict):

    people = [person1, person2, person3]
    lowest = 30 
    name = ""
    for person in people:
        sum = 0
        for i in range(1,4):
            sum += person[f"result{i}"]
        if sum < lowest:
            lowest = sum
            name = person
    return name

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

