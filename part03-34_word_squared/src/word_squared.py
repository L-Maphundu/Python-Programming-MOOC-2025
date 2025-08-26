# Write your solution here
def squared(word, num):

    if len(word) < num**2:
        while True:
            word *= 2
            if len(word) >= num**2:
                break
        for i in range(num):
            print(word[:num])
            word = word[num:]
        
if __name__ == "__main__":
    squared('ab',3)