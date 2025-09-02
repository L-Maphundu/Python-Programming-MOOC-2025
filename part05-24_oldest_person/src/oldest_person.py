# Write your solution here
def oldest_person(people: list):
    ages = []
    for age in people:
        ages.append(age[1])

    for person in people:
        if person[1] == min(ages):
            return person[0]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [('Emily', 2014), ('Arthur', 1977), ('Ernest', 1985), ('Mary', 1953), ('Ellen', 1997)]
    print(oldest_person(people))