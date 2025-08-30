# Write your solution here
def factorials(n):
    """Creates a dictionary of factorials for
    1 to n."""

    factorials = {}
    j = 1

    for i in range(1, n + 1):
        j *= i
        factorials[i] = j
        
    return factorials

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])