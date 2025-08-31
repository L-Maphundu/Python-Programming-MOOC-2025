# Write your solution here
def histogram(string):
    histogram = {}

    for char in string:
        if char not in histogram:
            histogram[char] = "*"
        else:
            histogram[char] += "*"
    
    for key in histogram:
        print(key, histogram[key])

if __name__ == "__main__":
    histogram("statistically")
