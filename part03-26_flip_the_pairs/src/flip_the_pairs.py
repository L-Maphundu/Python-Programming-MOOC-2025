# Write your solution here
def reverse_pairs(odds,evens):
        k = 0
        j = 0
        for i in range(1, (len(odds) + len(evens)) + 1):
            if i % 2 != 0:
                print(evens[j])
                j += 1
            else:
                print(odds[k])
                k += 1
def main():
    number = int(input("Please type in a number: "))
    odds = []
    evens = []
    for i in range(1,number + 1):
        if i % 2 != 0:
            odds.append(i)
        else:
            evens.append(i)

    if len(odds) == len(evens):
        reverse_pairs(odds,evens)
    else:
        last = odds[len(odds)-1]
        odds = odds[:len(odds) - 1]
        reverse_pairs(odds,evens)
        print(last)
main()